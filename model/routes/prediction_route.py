from flask import Blueprint, Response, request
from services import request_service as req
from services.request_service import PredictionRequestValidity
from services import constants_service as ct
from services import extractor_service as ex
from services import response_service as res
import time
from services.monitoring import REQUESTS, IN_PROGRESS, LAST, LATENCY, HISTOGRAM_LATENCY, REQUEST_TIME


# Create the prediction route
app_prediction = Blueprint('predict', __name__)


@REQUEST_TIME.time()
@app_prediction.route('', methods=['POST'])
def predict() -> Response:
    """
    Return a 200 OK Flask Response containing the extracted toxicity statistics
    from the request JSON "input" component if the input is valid,
    otherwise return a 400 Bad Request.
    :return: the extracted toxicity statistics
    """
    start = time.time()
    REQUESTS.inc()
    IN_PROGRESS.inc()
    request_validity = req.get_prediction_request_validity(request.json)
    if req.is_invalid_request_json(request_validity):
        _set_served_request_metrics(start)
        return _send_400_response(request_validity)
    user_input = request.json[ct.get_prediction_endpoint_key()]
    extractor_response = ex.get_toxicity_stats(user_input)
    _set_served_request_metrics(start)
    return res.get_200_response(extractor_response)


def _send_400_response(request_validity: PredictionRequestValidity) -> Response:
    """
    Return a 400 Bad Request Flask Response from the given request invalidity reason
    (must not be PredictionRequestValidity.VALID otherwise will raise ValueError).
    :param request_validity: the given request invalidity reason (must not be PredictionRequestValidity.VALID).
    :return: a 400 Bad Request Flask Response from the given request invalidity reason
    """
    if request_validity is PredictionRequestValidity.VALID:
        raise ValueError('The provided request_validity must not be PredictionRequestValidity.VALID.')
    error_message = req.get_prediction_model_error_message_by_validity(request_validity)
    return res.get_400_response(error_message)


def _set_served_request_metrics(start: float):
    """
    Set the served request metrics.
    :param start: Received request time
    """
    LAST.set(time.time())
    IN_PROGRESS.dec()
    LATENCY.observe(time.time() - start)
    HISTOGRAM_LATENCY.observe(time.time() - start)
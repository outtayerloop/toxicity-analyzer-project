from enum import Enum
from typing import Optional
from services import constants_service as ct


# Prediction request validity enumerator
class PredictionRequestValidity(Enum):
    VALID = 1
    NONE_JSON_REQUEST_BODY = 2
    MISSING_INPUT_KEY = 3
    NONE_INPUT_KEY = 4
    TOO_BIG_INPUT = 5


def get_prediction_request_validity(request_json: Optional[dict[str, str]]) -> PredictionRequestValidity:
    """
    Return whether the provided json input is valid
    or has a None JSON request body
    or has no input key
    or has a None input value
    or has a too big input value.
    :param request_json: the user input provided from the JSON request object
    :return: a PredictionRequestValidity enumerator object with the associated validity value of the request JSON input.
    """
    input_key = ct.get_prediction_endpoint_key()
    if request_json is None:
        return PredictionRequestValidity.NONE_JSON_REQUEST_BODY
    elif input_key not in request_json:
        return PredictionRequestValidity.MISSING_INPUT_KEY
    elif request_json[input_key] is None or request_json[input_key].strip(' ') == '':
        return PredictionRequestValidity.NONE_INPUT_KEY
    elif len(request_json[input_key]) > ct.get_max_input_length():
        return PredictionRequestValidity.TOO_BIG_INPUT
    else:
        return PredictionRequestValidity.VALID


def is_invalid_request_json(request_validity: PredictionRequestValidity) -> bool:
    """
    Return True if the provided validity enumerator contains the value VALID,
    otherwise return False.
    :param request_validity: the user input provided from the JSON request object
    :return: True if the input is invalid, else False
    """
    return request_validity is not PredictionRequestValidity.VALID


def get_prediction_model_error_message_by_validity(request_validity: PredictionRequestValidity) -> str:
    """
    Return the error message associated to the provided request validity for each identified issue.
    Must not be PredictionRequestValidity.VALID and must be implemented, otherwise will raise ValueError.
    :param request_validity: The input request JSON
    :return: the dictionary containing the relevant error message
    """
    if request_validity is PredictionRequestValidity.NONE_JSON_REQUEST_BODY:
        error_message = ct.get_none_json_request_body_message()
    elif request_validity is PredictionRequestValidity.MISSING_INPUT_KEY:
        error_message = ct.get_missing_input_key_message()
    elif request_validity is PredictionRequestValidity.NONE_INPUT_KEY:
        error_message = ct.get_none_input_key_message()
    elif request_validity is PredictionRequestValidity.TOO_BIG_INPUT:
        error_message = ct.get_too_big_input_length_message()
    else:
        # Either lack of implementation or a PredictionRequestValidity.VALID validity was provided when forbidden.
        raise ValueError(ct.get_bad_provided_validity_exception_message())
    return error_message
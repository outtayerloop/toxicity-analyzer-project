from flask import Blueprint, Response
from services import response_service as res


# Create the e2e tests route
app_e2e = Blueprint('e2e', __name__)


@app_e2e.route('', methods=['GET'])
def test() -> Response:
    """
    Return a 200 OK Flask Response without content.
    :return: a 200 OK Flask Response without content.
    """
    return res.get_200_response()
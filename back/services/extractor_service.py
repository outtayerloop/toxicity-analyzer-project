import requests
from dotenv import load_dotenv
import os
from services import constants_service as ct
import json


# Take environment variables from .env file
load_dotenv()

# Prediction model host environment variable
prediction_model_host = os.getenv(ct.get_prediction_model_host_env_variable_label())

# Prediction model port environment variable
prediction_model_port = str(os.getenv(ct.get_prediction_model_port_env_variable_label()))


def get_toxicity_stats(user_input: str) -> dict[str, str]:
    """
    Return a dict containing the extracted toxicity statistics from the input text.
    This will make an HTTP POST call to the prediction endpoint.
    :param user_input: provided input text
    :return: the extracted toxicity statistics with a two-decimals precision
    """
    prediction_endpoint_url = f'http://{prediction_model_host}:{prediction_model_port}/predict'
    json_content = json.dumps({ct.get_prediction_model_endpoint_key(): user_input})
    headers = {'content-type': ct.get_application_content_type()}
    response = requests.post(prediction_endpoint_url, data=json_content, headers=headers)
    content = json.loads(response.content.decode('utf-8'))
    prediction_content_key = ct.get_prediction_model_response_content_key()
    return content[prediction_content_key]
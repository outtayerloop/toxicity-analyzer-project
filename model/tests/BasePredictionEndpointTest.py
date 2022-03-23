from typing import Optional, Union

import requests
import json

from dotenv import load_dotenv

from services import constants_service as ct
import os

# Take environment variables from .env file
load_dotenv()


# Prediction model host environment variable
host = os.getenv(ct.get_prediction_model_host_env_variable_label())

# Prediction model port environment variable
port = str(os.getenv(ct.get_prediction_model_port_env_variable_label()))

# Get prediction model endpoint URL prefix
url_prefix = ct.get_prediction_endpoint_url_prefix()


class BasePredictionEndpointTest:

    # Prediction model endpoint full URL
    prediction_model_endpoint_base_url = f'http://{host}:{port}/{url_prefix}'

    # Mock valid user input
    valid_user_input = 'x' * ct.get_max_input_length()

    # Prediction endpoint dictionary content key
    content_key = ct.get_response_content_key()

    # Expected minimum component percentage
    expected_minimum_component_percentage = ct.get_component_threshold()

    # Valid content dict
    valid_content = {ct.get_prediction_endpoint_key(): valid_user_input}

    # Valid content JSON
    valid_json_content = json.dumps(valid_content)

    # Request headers
    valid_headers = {'content-type': ct.get_application_content_type()}

    def get_prediction_endpoint_response_body(self, content_dict: Optional[dict[str, str]], has_headers: bool) \
            -> dict[str, Union[str, dict[str, str]]]:
        """
        Return the prediction endpoint's response body from the provided input content
        :param content_dict: dictionary content to be jsonified and sent to the prediction endpoint
        :param has_headers: determines whether or not application content headers should be set
        :return: a dictionary object obtained from a POST request issued from the requests module
        """
        content_json = json.dumps(content_dict)
        headers = self.valid_headers if has_headers else None
        response = requests.post(self.prediction_model_endpoint_base_url, data=content_json, headers=headers)
        return json.loads(response.content.decode('utf-8'))
from typing import Optional, Union
import requests
import json
from dotenv import load_dotenv
from services import constants_service as ct
import os

# Take environment variables from .env file
load_dotenv()

# Analyzer endpoint host environment variable
host = os.getenv(ct.get_analyzer_endpoint_host_env_variable_label())

# Analyzer endpoint port environment variable
port = str(os.getenv(ct.get_analyzer_endpoint_port_env_variable_label()))

# Get analyzer endpoint URL prefix
url_prefix = ct.get_analyzer_endpoint_url_prefix()


class BaseAnalyzerEndpointTest:

    # Analyzer endpoint full URL
    analyzer_endpoint_base_url = f'http://{host}:{port}/{url_prefix}'

    # Mock valid user input
    valid_user_input = 'x' * ct.get_max_input_length()

    # Analyzer endpoint dictionary content key
    content_key = ct.get_response_content_key()

    # Expected minimum component percentage
    expected_minimum_component_percentage = ct.get_component_threshold()

    # Valid content dict
    valid_content = {ct.get_analyzer_endpoint_key(): valid_user_input}

    # Valid content JSON
    valid_json_content = json.dumps(valid_content)

    # Request headers
    valid_headers = {'content-type': ct.get_application_content_type()}

    def get_analyzer_endpoint_response_body(self, content_dict: Optional[dict[str, str]], has_headers: bool) -> dict[str, Union[str, dict[str, str]]]:
        """
        Return the analyzer endpoint's response body from the provided input content
        :param content_dict: dictionary content to be jsonified and sent to the analyzer endpoint
        :param has_headers: determines whether or not application content headers should be set
        :return: a dictionary object obtained from a POST request issued from the requests module
        """
        json_content = json.dumps(content_dict)
        headers = self.valid_headers if has_headers is True else None
        response = requests.post(self.analyzer_endpoint_base_url, data=json_content, headers=headers)
        return json.loads(response.content.decode('utf-8'))

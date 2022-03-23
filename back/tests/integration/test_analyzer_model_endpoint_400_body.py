from services import constants_service as ct
from tests.BaseAnalyzerEndpointTest import BaseAnalyzerEndpointTest


class TestAnalyzerEndpoint400Body(BaseAnalyzerEndpointTest):

    def test_none_json_body_returns_400_none_json_request_body_message(self):
        """
        Test if sending a request with None JSON body to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_none_json_request_body_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        invalid_content = None
        actual_body = super().get_analyzer_endpoint_response_body(invalid_content, True)
        assert actual_body == expected_body

    def test_missing_json_content_type_headers_returns_400_none_json_request_body_message(self):
        """
        Test if sending a request with a valid JSON body
        and missing content type application/json headers to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_none_json_request_body_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        valid_content = {ct.get_analyzer_endpoint_key(): self.valid_user_input}
        actual_body = super().get_analyzer_endpoint_response_body(valid_content, False)
        assert actual_body == expected_body

    def test_empty_json_body_returns_400_missing_input_key_body_message(self):
        """
        Test if sending a request with empty JSON body to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_missing_input_key_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        invalid_content = {}
        actual_body = super().get_analyzer_endpoint_response_body(invalid_content, True)
        assert actual_body == expected_body

    def test_invalid_json_key_returns_400_missing_input_key_body_message(self):
        """
        Test if sending a request with missing "input" key to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_missing_input_key_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        invalid_key = 'invalid_key'
        invalid_content = {invalid_key: self.valid_user_input}
        actual_body = super().get_analyzer_endpoint_response_body(invalid_content, True)
        assert actual_body == expected_body

    def test_none_json_input_key_returns_400_none_input_key_body_message(self):
        """
        Test if sending a request with None "input" key to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_none_input_key_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        none_input = None
        invalid_content = {ct.get_analyzer_endpoint_key(): none_input}
        actual_body = super().get_analyzer_endpoint_response_body(invalid_content, True)
        assert actual_body == expected_body

    def test_whitespace_json_input_key_returns_400_none_input_key_body_message(self):
        """
        Test if sending a request with full whitespace "input" key to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_none_input_key_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        whitespace_input = ' '
        invalid_content = {ct.get_analyzer_endpoint_key(): whitespace_input}
        actual_body = super().get_analyzer_endpoint_response_body(invalid_content, True)
        assert actual_body == expected_body

    def test_empty_json_input_key_returns_400_none_input_key_body_message(self):
        """
        Test if sending a request with an empty "input" key to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_none_input_key_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        empty_input = ''
        invalid_content = {ct.get_analyzer_endpoint_key(): empty_input}
        actual_body = super().get_analyzer_endpoint_response_body(invalid_content, True)
        assert actual_body == expected_body

    def test_too_big_json_input_returns_400_too_big_input_length_body_message(self):
        """
        Test if sending a request with too big "input" key to the analyzer endpoint route
        results in the expected 400 Bad Request response message.
        """
        expected_response_message = ct.get_too_big_input_length_message()
        expected_body = {ct.get_response_message_key(): expected_response_message}
        too_big_input = 'x' * (ct.get_max_input_length() + 1)
        invalid_content = {ct.get_analyzer_endpoint_key(): too_big_input}
        actual_body = super().get_analyzer_endpoint_response_body(invalid_content, True)
        assert actual_body == expected_body
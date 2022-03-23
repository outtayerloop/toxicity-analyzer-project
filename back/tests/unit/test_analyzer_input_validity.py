from services import request_service as req
from services.request_service import AnalyzerRequestValidity
from services import constants_service as ct
import pytest


class TestPredictionInputValidity:

    def test_none_request_json_returns_none_json_request_body_validity(self):
        """
        Test if the AnalyzerRequestValidity value returned by the corresponding method of the request validity service
        is NONE_JSON_REQUEST_BODY when the provided input is None.
        """
        expected_validity = AnalyzerRequestValidity.NONE_JSON_REQUEST_BODY
        invalid_request_json = None
        actual_validity = req.get_analyzer_request_validity(invalid_request_json)
        assert actual_validity is expected_validity

    def test_no_request_json_input_key_returns_missing_input_key(self):
        """
        Test if the AnalyzerRequestValidity value returned by the corresponding method of the request validity service
        is MISSING_INPUT_KEY when the provided JSON input is empty.
        """
        expected_validity = AnalyzerRequestValidity.MISSING_INPUT_KEY
        invalid_request_json = {}
        actual_validity = req.get_analyzer_request_validity(invalid_request_json)
        assert actual_validity is expected_validity

    def test_none_request_json_input_value_returns_none_input_key(self):
        """
        Test if the AnalyzerRequestValidity value returned by the corresponding method of the request validity service
        is NONE_INPUT_KEY when the provided input key is None.
        """
        expected_validity = AnalyzerRequestValidity.NONE_INPUT_KEY
        input_key = ct.get_analyzer_endpoint_key()
        invalid_request_json = {input_key: None}
        actual_validity = req.get_analyzer_request_validity(invalid_request_json)
        assert actual_validity is expected_validity

    def test_too_big_input_returns_too_big_input(self):
        """
        Test if the AnalyzerRequestValidity value returned by the corresponding method of the request validity service
        is TOO_BIG_INPUT when the provided input is too big.
        """
        expected_validity = AnalyzerRequestValidity.TOO_BIG_INPUT
        input_key = ct.get_analyzer_endpoint_key()
        too_big_input = 'x' * (ct.get_max_input_length() + 1)
        invalid_request_json = {input_key: too_big_input}
        actual_validity = req.get_analyzer_request_validity(invalid_request_json)
        assert actual_validity is expected_validity

    def test_valid_input_returns_valid(self):
        """
        Test if the AnalyzerRequestValidity value returned by the corresponding method of the request validity service
        is VALID when the provided input is valid.
        """
        expected_validity = AnalyzerRequestValidity.VALID
        input_key = ct.get_analyzer_endpoint_key()
        valid_input = 'x' * ct.get_max_input_length()
        valid_request_json = {input_key: valid_input}
        actual_validity = req.get_analyzer_request_validity(valid_request_json)
        assert actual_validity is expected_validity

    def test_none_json_request_body_validity_returns_none_json_request_body_message(self):
        """
        Test if the message associated with missing headers or None request body JSON is the expected one.
        """
        expected_message = ct.get_none_json_request_body_message()
        actual_message = req.get_analyzer_error_message_by_validity(AnalyzerRequestValidity.NONE_JSON_REQUEST_BODY)
        assert actual_message == expected_message

    def test_missing_request_json_input_key_returns_missing_input_key_message(self):
        """
        Test if the message associated with missing input key is the expected one.
        """
        expected_message = ct.get_missing_input_key_message()
        actual_message = req.get_analyzer_error_message_by_validity(AnalyzerRequestValidity.MISSING_INPUT_KEY)
        assert actual_message == expected_message

    def test_none_request_json_input_key_returns_none_input_key_message(self):
        """
        Test if the message associated with None input key is the expected one.
        """
        expected_message = ct.get_none_input_key_message()
        actual_message = req.get_analyzer_error_message_by_validity(AnalyzerRequestValidity.NONE_INPUT_KEY)
        assert actual_message == expected_message

    def test_valid_input_to_error_message_returns_exception_message(self):
        """
        Test if the message associated with a too big input length is the expected one.
        """
        expected_message = ct.get_bad_provided_validity_exception_message()
        with pytest.raises(ValueError, match=expected_message):
            req.get_analyzer_error_message_by_validity(AnalyzerRequestValidity.VALID)

    def test_valid_validity_value_against_invalidity_check_returns_false(self):
        """
        Test if checking for an invalid status on a VALID AnalyzerRequestValidity input value
        returns False.
        """
        expected_check_result = False
        actual_check_result = req.is_invalid_request_json(AnalyzerRequestValidity.VALID)
        return actual_check_result == expected_check_result

    def test_none_json_request_body_validity_value_against_invalidity_check_returns_true(self):
        """
        Test if checking for an invalid status on a NONE_JSON_REQUEST_BODY AnalyzerRequestValidity input value
        returns True.
        """
        expected_check_result = True
        actual_check_result = req.is_invalid_request_json(AnalyzerRequestValidity.NONE_JSON_REQUEST_BODY)
        return actual_check_result == expected_check_result

    def test_missing_input_key_validity_value_against_invalidity_check_returns_true(self):
        """
        Test if checking for an invalid status on a MISSING_INPUT_KEY AnalyzerRequestValidity input value
        returns True.
        """
        expected_check_result = True
        actual_check_result = req.is_invalid_request_json(AnalyzerRequestValidity.MISSING_INPUT_KEY)
        return actual_check_result == expected_check_result

    def test_none_input_key_validity_value_against_invalidity_check_returns_true(self):
        """
        Test if checking for an invalid status on a NONE_INPUT_KEY AnalyzerRequestValidity input value
        returns True.
        """
        expected_check_result = True
        actual_check_result = req.is_invalid_request_json(AnalyzerRequestValidity.NONE_INPUT_KEY)
        return actual_check_result == expected_check_result

    def test_too_big_input_validity_value_against_invalidity_check_returns_true(self):
        """
        Test if checking for an invalid status on a TOO_BIG_INPUT AnalyzerRequestValidity input value
        returns True.
        """
        expected_check_result = True
        actual_check_result = req.is_invalid_request_json(AnalyzerRequestValidity.TOO_BIG_INPUT)
        return actual_check_result == expected_check_result
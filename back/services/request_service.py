from enum import Enum
from typing import Optional
from services import constants_service as ct


# Analyzer request validity enumerator
class AnalyzerRequestValidity(Enum):
    VALID = 1
    NONE_JSON_REQUEST_BODY = 2
    MISSING_INPUT_KEY = 3
    NONE_INPUT_KEY = 4
    TOO_BIG_INPUT = 5


def get_analyzer_request_validity(request_json: Optional[dict[str, str]]) -> AnalyzerRequestValidity:
    """
    Return whether the provided json input is valid
    or has a None JSON request body
    or has no input key
    or has a None input value
    or has a too big input value.
    :param request_json: the user input provided from the JSON request object
    :return: a AnalyzerRequestValidity enumerator object with the associated validity value of the request JSON input.
    """
    input_key = ct.get_analyzer_endpoint_key()
    if request_json is None:
        return AnalyzerRequestValidity.NONE_JSON_REQUEST_BODY
    elif input_key not in request_json:
        return AnalyzerRequestValidity.MISSING_INPUT_KEY
    elif request_json[input_key] is None or request_json[input_key].strip(' ') == '':
        return AnalyzerRequestValidity.NONE_INPUT_KEY
    elif len(request_json[input_key]) > ct.get_max_input_length():
        return AnalyzerRequestValidity.TOO_BIG_INPUT
    else:
        return AnalyzerRequestValidity.VALID


def is_invalid_request_json(request_validity: AnalyzerRequestValidity) -> bool:
    """
    Return True if the provided validity enumerator contains the value VALID,
    otherwise return False.
    :param request_validity: the user input provided from the JSON request object
    :return: True if the input is invalid, else False
    """
    return request_validity is not AnalyzerRequestValidity.VALID


def get_analyzer_error_message_by_validity(request_validity: AnalyzerRequestValidity) -> str:
    """
    Return the error message associated to the provided request validity for each identified issue.
    Must not be AnalyzerRequestValidity.VALID and must be implemented, otherwise will raise ValueError.
    :param request_validity: The input request JSON
    :return: the dictionary containing the relevant error message
    """
    if request_validity is AnalyzerRequestValidity.NONE_JSON_REQUEST_BODY:
        error_message = ct.get_none_json_request_body_message()
    elif request_validity is AnalyzerRequestValidity.MISSING_INPUT_KEY:
        error_message = ct.get_missing_input_key_message()
    elif request_validity is AnalyzerRequestValidity.NONE_INPUT_KEY:
        error_message = ct.get_none_input_key_message()
    elif request_validity is AnalyzerRequestValidity.TOO_BIG_INPUT:
        error_message = ct.get_too_big_input_length_message()
    else:
        # Either lack of implementation or a AnalyzerRequestValidity.VALID validity was provided when forbidden.
        raise ValueError(ct.get_bad_provided_validity_exception_message())
    return error_message
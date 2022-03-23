from services import extractor_service as ex
from services import constants_service as ct


def get_user_input_actual_component_percentage(user_input: str, component_label: str) -> float:
    """
    Return the provided component percentage given by the extractor service from the provided user input.
    :param user_input: provided sentence
    :param component_label: the component from which to return the extracted percentage
    :return: the provided component percentage given by the extractor service from the provided user input.
    """
    actual_extraction = ex.get_toxicity_stats(user_input)
    return float(actual_extraction[component_label])


class BaseExtractorTest:

    # Expected minimum component percentage
    expected_minimum_component_percentage = ct.get_component_threshold()
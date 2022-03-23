from tests.BasePredictionEndpointTest import BasePredictionEndpointTest
from services import constants_service as ct


class TestPredictionModelEndpointThreat(BasePredictionEndpointTest):

    # Prediction endpoint dictionary threat rate label
    threat_label = ct.get_threat_label()

    def test_basic_threatening_sentence_without_punctuation_returns_threat_response_body(self):
        """
        Test if a basic threatening input
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I will kill you'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_basic_threatening_sentence_with_punctuation_emphasis_returns_threat_response_body(self):
        """
        Test if a basic threatening input with an exclamation point
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I will kill you!'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_basic_threatening_sentence_with_capitalization_emphasis_returns_threat_response_body(self):
        """
        Test if basic threatening input with the word with the most impact capitalized
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I will KILL you'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_booster_words_returns_threat_response_body(self):
        """
        Test if a threatening input with threat rate booster words
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I will kill you, slaughter you'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_booster_words_with_capitalization_emphasis_returns_threat_response_body(self):
        """
        Test if a threatening input with capitalized threat rate booster words
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I will KILL you, SLAUGHTER you'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_slang_without_punctuation_emphasis_handling_returns_threat_response_body(self):
        """
        Test if a threatening input with slang
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'i\'mma kill u'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_slang_with_punctuation_emphasis_handling_returns_threat_response_body(self):
        """
        Test if a threatening input with slang and an exclamation point
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'i\'mma kill u!'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_slang_with_punctuation_and_capitalization_emphasis_handling_returns_threat_response_body(self):
        """
        Test if a threatening input with capitalized slang and an exclamation point
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I\'MMA kill U!'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_sentence_with_time_notion_without_punctuation_returns_threat_response_body(self):
        """
        Test if a threatening input with time influence marker
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I have always wanted to kill you, now I will'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_sentence_with_time_notion_with_punctuation_emphasis_returns_threat_response_body(self):
        """
        Test if a threatening input with time influence marker and an exclamation point
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I have always wanted to kill you, now I will!'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_sentence_with_time_notion_with_capitalization_emphasis_returns_threat_response_body(self):
        """
        Test if a threatening input with capitalized time influence marker
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I have ALWAYS WANTED to kill you, NOW I WILL!'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_qualified_threatening_sentence_without_punctuation_returns_threat_response_body(self):
        """
        Test if a qualified threatening input
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I kind of want to kill you'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_qualified_threatening_sentence_with_punctuation_emphasis_returns_threat_response_body(self):
        """
        Test if a qualified threatening input and an exclamation point
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I kind of want to kill you!'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_qualified_threatening_sentence_with_capitalization_emphasis_returns_threat_response_body(self):
        """
        Test if a capitalized qualified threatening input with
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I KIND OF want to kill you'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_threatening_mixed_negation_sentence_returns_threat_response_body(self):
        """
        Test if a mixed threatening negation input
        results in a response JSON body with a threat rate label value overcoming or equal to the threat rate threshold.
        """
        threatening_sentence = 'I want to hug you but I want to kill you at the same time'
        actual_threat_rate = self._get_user_input_actual_threat_rate(threatening_sentence)
        assert actual_threat_rate >= self.expected_minimum_component_percentage

    def test_nice_sentence_returns_nice_response_body(self):
        """
        Test if a nice input results in a response JSON body with a threat rate label value
        inferior to the threat rate threshold.
        """
        nice_sentence = 'I love everyone'
        actual_threat_rate = self._get_user_input_actual_threat_rate(nice_sentence)
        assert actual_threat_rate < self.expected_minimum_component_percentage

    def _get_user_input_actual_threat_rate(self, user_input: str) -> float:
        """
        Return the threat percentage given by the prediction endpoint from the provided user input.
        :param user_input: provided sentence
        :return: the threat percentage given by the prediction endpoint from the provided user input.
        """
        threatening_content = {ct.get_prediction_endpoint_key(): user_input}
        actual_body = super().get_prediction_endpoint_response_body(threatening_content, True)
        return float(actual_body[self.content_key][self.threat_label])
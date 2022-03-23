from tests.BaseAnalyzerEndpointTest import BaseAnalyzerEndpointTest
from services import constants_service as ct


class TestAnalyzerBackEndpointInsult(BaseAnalyzerEndpointTest):

    # Prediction endpoint dictionary insult label
    insult_label = ct.get_insult_label()

    def test_basic_insult_sentence_without_punctuation_returns_insult_response_body(self):
        """
        Test if a basic insult input
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You motherf*****'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_basic_insult_sentence_with_punctuation_emphasis_returns_insult_response_body(self):
        """
        Test if a basic insult input with an exclamation point
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You motherf*****!'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_basic_insult_sentence_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if a basic insult input with the word with the most impact capitalized
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You MOTHERF*****!'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_booster_words_returns_insult_response_body(self):
        """
        Test if an insult input with insult booster words
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You motherf*****, son of a b****'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_booster_words_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if an insult input with capitalized insult booster words
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You MOTHERF*****, SON of a B****'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_slang_without_punctuation_emphasis_handling_returns_insult_response_body(self):
        """
        Test if an insult input with slang
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'If you breath, you a thooot'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_slang_with_punctuation_emphasis_handling_returns_insult_response_body(self):
        """
        Test if an insult input with slang and an exclamation point
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'If you breath, you a thooot!'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_slang_with_punctuation_and_capitalization_emphasis_handling_returns_insult_response_body(self):
        """
        Test if an insult input with capitalized slang and an exclamation point
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'If you breath, you a THOOOT!'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_sentence_with_time_notion_without_punctuation_returns_insult_response_body(self):
        """
        Test if an insult input with time influence marker
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'ve always been a son of a b****'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_sentence_with_time_notion_with_punctuation_emphasis_returns_insult_response_body(self):
        """
        Test if an insult input with time influence marker and an exclamation point
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'ve always been a son of a b****!'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_sentence_with_time_notion_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if an insult input with capitalized time influence marker
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'ve ALWAYS been a SON of a B****!'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_qualified_insult_sentence_without_punctuation_returns_insult_response_body(self):
        """
        Test if a qualified insult input
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'re kind of an a**hole'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_qualified_insult_sentence_with_punctuation_emphasis_returns_insult_response_body(self):
        """
        Test if a qualified insult input and an exclamation point
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'re kind of an a**hole'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_qualified_insult_sentence_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if a capitalized qualified insult input with
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'re KIND OF an a**hole'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_mixed_negation_sentence_returns_insult_response_body(self):
        """
        Test if a mixed insult negation input
        results in a response JSON body with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'I love chocolate a lot, but you\'re the biggest dumb*** i\'ve ever met'
        actual_insult_rate = self._get_user_input_actual_insult_rate(insult_sentence)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_nice_sentence_returns_nice_response_body(self):
        """
        Test if a nice input results in a response JSON body with an insult rate label value
        inferior to the insult rate threshold.
        """
        nice_sentence = 'I love everyone'
        actual_insult_rate = self._get_user_input_actual_insult_rate(nice_sentence)
        assert actual_insult_rate < self.expected_minimum_component_percentage

    def _get_user_input_actual_insult_rate(self, user_input: str) -> float:
        """
        Return the insult percentage given by the prediction endpoint from the provided user input.
        :param user_input: provided sentence
        :return: the insult percentage given by the prediction endpoint from the provided user input.
        """
        insult_content = {ct.get_analyzer_endpoint_key(): user_input}
        actual_body = super().get_analyzer_endpoint_response_body(insult_content, True)
        return float(actual_body[self.content_key][self.insult_label])
from tests.BaseAnalyzerEndpointTest import BaseAnalyzerEndpointTest
from services import constants_service as ct


class TestAnalyzerBackEndpointObscenity(BaseAnalyzerEndpointTest):

    # Prediction endpoint dictionary obscenity label
    obscenity_label = ct.get_obscenity_label()

    def test_basic_obscene_sentence_without_punctuation_returns_obscenity_response_body(self):
        """
        Test if a basic obscene input
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'My d*** in your a**'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_basic_obscene_sentence_with_punctuation_emphasis_returns_obscenity_response_body(self):
        """
        Test if a basic obscene input with an exclamation point
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'My d*** in your a**!'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_basic_obscene_sentence_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if a basic obscene input with the word with the most impact capitalized
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'My D*** in your A**'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_booster_words_returns_obscenity_response_body(self):
        """
        Test if an obscene input with obscenity booster words
        results in a response JSON body with a obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in your a** sweating hard'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_booster_words_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if an obscene input with capitalized obscenity booster words
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in your a** SWEATING hard'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_slang_without_punctuation_emphasis_handling_returns_obscenity_response_body(self):
        """
        Test if an obscene input with slang
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in ur a**'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_slang_with_punctuation_emphasis_handling_returns_obscenity_response_body(self):
        """
        Test if an obscene input with slang and an exclamation point
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in ur a**!'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_slang_with_punctuation_and_capitalization_emphasis_handling_returns_obscenity_response_body(self):
        """
        Test if an obscene input with capitalized slang and an exclamation point
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in UR a**!'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_sentence_with_time_notion_without_punctuation_returns_obscenity_response_body(self):
        """
        Test if an obscene input with time influence marker
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s always been a sl**'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_sentence_with_time_notion_with_punctuation_emphasis_returns_obscenity_response_body(self):
        """
        Test if an obscene input with time influence marker and an exclamation point
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s always been a sl**!'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_sentence_with_time_notion_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if an obscene input with capitalized time influence marker
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s ALWAYS BEEN a sl**!'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_qualified_obscene_sentence_without_punctuation_returns_obscenity_response_body(self):
        """
        Test if a qualified obscene input
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s at least kind of a sl**'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_qualified_obscene_sentence_with_punctuation_emphasis_returns_obscenity_response_body(self):
        """
        Test if a qualified obscene input and an exclamation point
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s at least kind of a sl**!'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_qualified_obscene_sentence_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if a capitalized qualified obscene input with
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s at least KIND OF a sl**'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_mixed_negation_sentence_returns_obscenity_response_body(self):
        """
        Test if a mixed obscene negation input
        results in a response JSON body with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'I love her a lot but, but she\'s such a sl** omg'
        actual_obscenity = self._get_user_input_actual_obscenity(obscene_sentence)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_nice_sentence_returns_nice_response_body(self):
        """
        Test if a nice input results in a response JSON body with an obscenity label value
        inferior to the obscenity rate threshold.
        """
        nice_sentence = 'I love everyone'
        actual_obscenity = self._get_user_input_actual_obscenity(nice_sentence)
        assert actual_obscenity < self.expected_minimum_component_percentage

    def _get_user_input_actual_obscenity(self, user_input: str) -> float:
        """
        Return the obscenity percentage given by the prediction endpoint from the provided user input.
        :param user_input: provided sentence
        :return: the obscenity percentage given by the prediction endpoint from the provided user input.
        """
        obscene_content = {ct.get_analyzer_endpoint_key(): user_input}
        actual_body = super().get_analyzer_endpoint_response_body(obscene_content, True)
        return float(actual_body[self.content_key][self.obscenity_label])
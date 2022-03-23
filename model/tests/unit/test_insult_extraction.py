from services import constants_service as ct
from tests.unit.BaseExtractorTest import BaseExtractorTest
from BaseExtractorTest import get_user_input_actual_component_percentage


class TestInsultExtraction(BaseExtractorTest):

    # Extractor service dictionary insult label
    insult_label = ct.get_insult_label()

    def test_basic_insult_sentence_without_punctuation_returns_insult_response_body(self):
        """
        Test if a basic insult input
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You motherf*****'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_basic_insult_sentence_with_punctuation_emphasis_returns_insult_response_body(self):
        """
        Test if a basic insult input with an exclamation point
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You motherf*****!'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_basic_insult_sentence_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if a basic insult input with the word with the most impact capitalized
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You MOTHERF*****!'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_booster_words_returns_insult_response_body(self):
        """
        Test if an insult input with insult booster words
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You motherf*****, son of a b****'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_booster_words_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if an insult input with capitalized insult booster words
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You MOTHERF*****, SON of a B****'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_slang_without_punctuation_emphasis_handling_returns_insult_response_body(self):
        """
        Test if an insult input with slang
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'If you breath, you a thooot'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_slang_with_punctuation_emphasis_handling_returns_insult_response_body(self):
        """
        Test if an insult input with slang and an exclamation point
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'If you breath, you a thooot!'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_slang_with_punctuation_and_capitalization_emphasis_handling_returns_insult_response_body(self):
        """
        Test if an insult input with capitalized slang and an exclamation point
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'If you breath, you a THOOOT!'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_sentence_with_time_notion_without_punctuation_returns_insult_response_body(self):
        """
        Test if an insult input with time influence marker
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'ve always been a son of a b****'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_sentence_with_time_notion_with_punctuation_emphasis_returns_insult_response_body(self):
        """
        Test if an insult input with time influence marker and an exclamation point
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'ve always been a son of a b****!'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_sentence_with_time_notion_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if an insult input with capitalized time influence marker
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'ve ALWAYS been a SON of a B****!'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_qualified_insult_sentence_without_punctuation_returns_insult_response_body(self):
        """
        Test if a qualified insult input
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'re kind of an a**hole'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_qualified_insult_sentence_with_punctuation_emphasis_returns_insult_response_body(self):
        """
        Test if a qualified insult input and an exclamation point
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'re kind of an a**hole'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_qualified_insult_sentence_with_capitalization_emphasis_returns_insult_response_body(self):
        """
        Test if a capitalized qualified insult input with
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'You\'re KIND OF an a**hole'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_insult_mixed_negation_sentence_returns_insult_response_body(self):
        """
        Test if a mixed insult negation input
        results in a dict with an insult label value overcoming or equal to the insult rate threshold.
        """
        insult_sentence = 'I love chocolate a lot, but you\'re the biggest dumb*** i\'ve ever met'
        actual_insult_rate = get_user_input_actual_component_percentage(insult_sentence, self.insult_label)
        assert actual_insult_rate >= self.expected_minimum_component_percentage

    def test_nice_sentence_returns_nice_response_body(self):
        """
        Test if a nice input results in a dict with an insult rate label value
        inferior to the insult rate threshold.
        """
        nice_sentence = 'I love everyone'
        actual_insult_rate = get_user_input_actual_component_percentage(nice_sentence, self.insult_label)
        assert actual_insult_rate < self.expected_minimum_component_percentage
from services import constants_service as ct
from tests.unit.BaseExtractorTest import BaseExtractorTest
from BaseExtractorTest import get_user_input_actual_component_percentage


class TestToxicityExtraction(BaseExtractorTest):

    # Extractor service dictionary toxicity label
    toxicity_label = ct.get_toxicity_label()

    def test_basic_toxic_sentence_without_punctuation_returns_toxicity_response_body(self):
        """
        Test if a basic toxic input
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I hate everything'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_basic_toxic_sentence_with_punctuation_emphasis_returns_toxicity_response_body(self):
        """
        Test if a basic toxic input with an exclamation point
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I hate everything!'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_basic_toxic_sentence_with_capitalization_emphasis_returns_toxicity_response_body(self):
        """
        Test if basic toxic input with the word with the most impact capitalized
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I HATE everything'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_booster_words_returns_toxicity_response_body(self):
        """
        Test if a toxic input with toxicity booster words
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I really hate you, despise you'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_booster_words_with_capitalization_emphasis_returns_toxicity_response_body(self):
        """
        Test if a toxic input with capitalized toxicity booster words
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I REALLY hate you, DESPISE you'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_slang_without_punctuation_emphasis_handling_returns_toxicity_response_body(self):
        """
        Test if a toxic input with slang
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'u mad'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_slang_with_punctuation_emphasis_handling_returns_toxicity_response_body(self):
        """
        Test if a toxic input with slang and an exclamation point
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'u mad!'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_slang_with_punctuation_and_capitalization_emphasis_handling_returns_toxicity_response_body(self):
        """
        Test if a toxic input with capitalized slang and an exclamation point
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'U MAD!'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_sentence_with_time_notion_without_punctuation_returns_toxicity_response_body(self):
        """
        Test if a toxic input with time influence marker
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I have always hated you'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_sentence_with_time_notion_with_punctuation_emphasis_returns_toxicity_response_body(self):
        """
        Test if a toxic input with time influence marker and an exclamation point
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I have always hated you!'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_sentence_with_time_notion_with_capitalization_emphasis_returns_toxicity_response_body(self):
        """
        Test if a toxic input with capitalized time influence marker
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I have ALWAYS HATED YOU!'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_qualified_toxic_sentence_without_punctuation_returns_toxicity_response_body(self):
        """
        Test if a qualified toxic input
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I kind of hate you'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_qualified_toxic_sentence_with_punctuation_emphasis_returns_toxicity_response_body(self):
        """
        Test if a qualified toxic input and an exclamation point
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I kind of hate you!'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_qualified_toxic_sentence_with_capitalization_emphasis_returns_toxicity_response_body(self):
        """
        Test if a capitalized qualified toxic input with
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I KIND OF hate you'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_toxic_mixed_negation_sentence_returns_toxicity_response_body(self):
        """
        Test if a mixed toxic negation input
        results in a dict with a toxicity label value overcoming or equal to the toxicity threshold.
        """
        toxic_sentence = 'I love chocolate a lot, but it sucks being here with you'
        actual_toxicity = get_user_input_actual_component_percentage(toxic_sentence, self.toxicity_label)
        assert actual_toxicity >= self.expected_minimum_component_percentage

    def test_nice_sentence_returns_nice_response_body(self):
        """
        Test if a nice input results in a dict with a toxicity label value
        inferior to the toxicity threshold.
        """
        nice_sentence = 'I love everyone'
        actual_toxicity = get_user_input_actual_component_percentage(nice_sentence, self.toxicity_label)
        assert actual_toxicity < self.expected_minimum_component_percentage
from services import constants_service as ct
from tests.unit.BaseExtractorTest import BaseExtractorTest
from BaseExtractorTest import get_user_input_actual_component_percentage


class TestObscenityExtraction(BaseExtractorTest):

    # Extractor service dictionary obscenity label
    obscenity_label = ct.get_obscenity_label()

    def test_basic_obscene_sentence_without_punctuation_returns_obscenity_response_body(self):
        """
        Test if a basic obscene input
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'My d*** in your a**'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_basic_obscene_sentence_with_punctuation_emphasis_returns_obscenity_response_body(self):
        """
        Test if a basic obscene input with an exclamation point
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'My d*** in your a**!'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_basic_obscene_sentence_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if a basic obscene input with the word with the most impact capitalized
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'My D*** in your A**'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_booster_words_returns_obscenity_response_body(self):
        """
        Test if an obscene input with obscenity booster words
        results in a dict with a obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in your a** sweating hard'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_booster_words_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if an obscene input with capitalized obscenity booster words
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in your a** SWEATING hard'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_slang_without_punctuation_emphasis_handling_returns_obscenity_response_body(self):
        """
        Test if an obscene input with slang
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in ur a**'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_slang_with_punctuation_emphasis_handling_returns_obscenity_response_body(self):
        """
        Test if an obscene input with slang and an exclamation point
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in ur a**!'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_slang_with_punctuation_and_capitalization_emphasis_handling_returns_obscenity_response_body(self):
        """
        Test if an obscene input with capitalized slang and an exclamation point
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'my d*** in UR a**!'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_sentence_with_time_notion_without_punctuation_returns_obscenity_response_body(self):
        """
        Test if an obscene input with time influence marker
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s always been a sl**'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_sentence_with_time_notion_with_punctuation_emphasis_returns_obscenity_response_body(self):
        """
        Test if an obscene input with time influence marker and an exclamation point
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s always been a sl**!'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_sentence_with_time_notion_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if an obscene input with capitalized time influence marker
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s ALWAYS BEEN a sl**!'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_qualified_obscene_sentence_without_punctuation_returns_obscenity_response_body(self):
        """
        Test if a qualified obscene input
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s at least kind of a sl**'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_qualified_obscene_sentence_with_punctuation_emphasis_returns_obscenity_response_body(self):
        """
        Test if a qualified obscene input and an exclamation point
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s at least kind of a sl**!'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_qualified_obscene_sentence_with_capitalization_emphasis_returns_obscenity_response_body(self):
        """
        Test if a capitalized qualified obscene input with
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'She\'s at least KIND OF a sl**'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_obscene_mixed_negation_sentence_returns_obscenity_response_body(self):
        """
        Test if a mixed obscene negation input
        results in a dict with an obscenity label value overcoming or equal to the obscenity threshold.
        """
        obscene_sentence = 'I love her a lot but, but she\'s such a sl** omg'
        actual_obscenity = get_user_input_actual_component_percentage(obscene_sentence, self.obscenity_label)
        assert actual_obscenity >= self.expected_minimum_component_percentage

    def test_nice_sentence_returns_nice_response_body(self):
        """
        Test if a nice input results in a dict with an obscenity label value
        inferior to the obscenity rate threshold.
        """
        nice_sentence = 'I love everyone'
        actual_obscenity = get_user_input_actual_component_percentage(nice_sentence, self.obscenity_label)
        assert actual_obscenity < self.expected_minimum_component_percentage
from services import constants_service as ct
from tests.unit.BaseExtractorTest import BaseExtractorTest
from BaseExtractorTest import get_user_input_actual_component_percentage


class TestPredictionModelEndpointIdentityAttack(BaseExtractorTest):

    # Extractor service dictionary identity attack label
    identity_attack_label = ct.get_identity_attack_label()

    def test_basic_identity_attack_sentence_without_punctuation_returns_identity_attack_response_body(self):
        """
        Test if a basic identity attack input
        results in a dict with an identity attack label value overcoming
        or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews suck'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_basic_identity_attack_sentence_with_punctuation_emphasis_returns_identity_attack_response_body(self):
        """
        Test if a basic identity attack input with an exclamation point
        results in a dict with an identity attack label value overcoming
        or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews suck!'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_basic_identity_attack_sentence_with_capitalization_emphasis_returns_identity_attack_response_body(self):
        """
        Test if basic identity attack input with the word with the most impact capitalized
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You ARABIC JEWS suck'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_booster_words_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with identity attack booster words
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'All of you arabic jews suck'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_booster_words_with_capitalization_emphasis_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with capitalized identity attack booster words
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'ALL OF YOU arabic jews suck'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_slang_without_punctuation_emphasis_handling_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with slang
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'Y\'all arabic jews suck'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_slang_with_punctuation_emphasis_handling_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with slang and an exclamation point
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'Y\'all arabic jews suck!'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_slang_with_punctuation_and_capitalization_emphasis_handling_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with capitalized slang and an exclamation point
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'Y\'ALL arabic jews suck!'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_sentence_with_time_notion_without_punctuation_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with time influence marker
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews have always sucked'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_sentence_with_time_notion_with_punctuation_emphasis_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with time influence marker and an exclamation point
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews have always sucked!'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_sentence_with_time_notion_with_capitalization_emphasis_returns_identity_attack_response_body(self):
        """
        Test if an identity attack input with capitalized time influence marker
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews HAVE ALWAYS sucked!'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_qualified_identity_attack_sentence_without_punctuation_returns_identity_attack_response_body(self):
        """
        Test if a qualified identity attack input
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews kind of suck'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_qualified_identity_attack_sentence_with_punctuation_emphasis_returns_identity_attack_response_body(self):
        """
        Test if a qualified identity attack input and an exclamation point
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews kind of suck!'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_qualified_identity_attack_sentence_with_capitalization_emphasis_returns_identity_attack_response_body(self):
        """
        Test if a capitalized qualified identity attack input with
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'You arabic jews KIND OF suck!'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_identity_attack_mixed_negation_sentence_returns_identity_response_body(self):
        """
        Test if a mixed identity attack negation input
        results in a dict with an identity attack label value overcoming
         or equal to the identity attack threshold.
        """
        identity_attack_sentence = 'I\'m not a discriminator but all of you arabic jews suck'
        actual_identity_attack = get_user_input_actual_component_percentage(identity_attack_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack >= self.expected_minimum_component_percentage

    def test_nice_sentence_returns_nice_response_body(self):
        """
        Test if a nice input results in a dict with an identity attack label value
        inferior to the identity attack threshold.
        """
        nice_sentence = 'I love everyone'
        actual_identity_attack = get_user_input_actual_component_percentage(nice_sentence,
                                                                            self.identity_attack_label)
        assert actual_identity_attack < self.expected_minimum_component_percentage
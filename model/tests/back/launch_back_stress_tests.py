from tests.back.BaseBackTestLaunch import BaseBackTestLaunch, BackEndTestType


class TestLaunchBackStressTests(BaseBackTestLaunch):

    def test_launch_back_stress_tests(self):
        """
        Launch the back-end stress tests and
        test if the exit code indicates success.
        """
        # Pytest exit code = 0 when all tests were collected and passed successfully.
        # See : https://docs.pytest.org/en/latest/reference/exit-codes.html
        test_type = BackEndTestType.STRESS
        completed_back_stress_tests_process = super().get_completed_back_tests_process_by_type(test_type)
        actual_exit_code = completed_back_stress_tests_process.returncode  # Associated exit code.
        assert actual_exit_code == self.expected_exit_code
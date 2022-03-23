from enum import Enum
import subprocess
from subprocess import CompletedProcess


# Back-end test type enumerator.
class BackEndTestType(Enum):
    INTEGRATION = 1
    STRESS = 2


class BaseBackTestLaunch:

    # Pytest exit code = 0 when all tests were collected and passed successfully.
    # See : https://docs.pytest.org/en/latest/reference/exit-codes.html
    expected_exit_code = 0

    back_integration_tests_folder = 'integration'

    back_stress_tests_folder = 'stress'

    def get_completed_back_tests_process_by_type(self, test_type: BackEndTestType) -> CompletedProcess:
        """
        Return the completed back-end tests process after running the specified test type.
        :param test_type: type of back-end tests to run (either integration or stress)
        :return: the completed back-end tests process after running the specified test type.
        """
        tests_folder = self.back_integration_tests_folder if test_type is BackEndTestType.INTEGRATION \
            else self.back_stress_tests_folder
        test_command = f'poetry run python -m pytest tests/{tests_folder}'
        launch_back_integration_tests_command = f'cd ../back && {test_command} && cd ../model'
        return subprocess.run(launch_back_integration_tests_command, shell=True)
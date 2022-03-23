import time
import futures3
import requests
from requests import Response
from tests.BaseAnalyzerEndpointTest import BaseAnalyzerEndpointTest
import datetime
import numpy as np


class TestStress(BaseAnalyzerEndpointTest):

    # Max expected response time in milliseconds (100 requests per minute SLA here)
    max_response_time_threshold = 600

    def test_analyzer_endpoint_200_response_time_when_single_request(self):
        """
        Test if sending single valid request to the analyzer endpoint
        does not take longer than the max accepted 200 OK response time threshold.
        """
        response = requests.post(self.analyzer_endpoint_base_url,
                                 data=self.valid_json_content,
                                 headers=self.valid_headers)
        response_time = response.elapsed.total_seconds() * 1000
        assert response_time <= self.max_response_time_threshold

    def test_analyzer_endpoint_stress_with_100_requests_per_minute_for_2_minutes(self):
        """
        Test if sending 100 valid requests per minute for 2 minutes to the analyzer endpoint
        results in an average response delay inferior or equal to the max accepted one.
        """
        url = self.analyzer_endpoint_base_url
        request_count_per_second = 2
        iteration_count = 2  # test for 2 minutes
        iteration_length = 50  # each period will be comprised of 50 seconds

        def do_post_to_analyzer_endpoint(current_url: str) -> Response:
            return requests.post(current_url, data=self.valid_json_content, headers=self.valid_headers)

        all_responses = []
        for i in range(0, iteration_count):
            begin_time_i = datetime.datetime.now()
            next_iteration_time_i = begin_time_i + datetime.timedelta(minutes=1)
            for j in range(0, iteration_length):  # we are going to send 2 request per second for 50 seconds
                begin_time_j = datetime.datetime.now()
                next_iteration_time_j = begin_time_j + datetime.timedelta(seconds=1)
                with futures3.ThreadPoolExecutor(max_workers=request_count_per_second) as pool:
                    responses = list(pool.map(do_post_to_analyzer_endpoint, [url] * request_count_per_second))
                    all_responses = all_responses + responses
                    end_time_j = datetime.datetime.now()
                if end_time_j < next_iteration_time_j:
                    remaining_sleep_time_j = (next_iteration_time_j - end_time_j).total_seconds()
                    time.sleep(remaining_sleep_time_j)
            end_time_i = datetime.datetime.now()
            if end_time_i < next_iteration_time_i and i < iteration_count - 1:
                remaining_sleep_time_i = (next_iteration_time_i - end_time_i).total_seconds()
                time.sleep(remaining_sleep_time_i)
        delays = list(map(lambda response: response.elapsed.total_seconds() * 1000, all_responses))
        assert np.mean(delays) <= self.max_response_time_threshold
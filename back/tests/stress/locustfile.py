from locust import HttpUser, task
from tests.BaseAnalyzerEndpointTest import BaseAnalyzerEndpointTest
from tests.ServerThread import start_server, stop_server

# Start the server before the tests begin
start_server()


class AnalyzerEndpointUser(HttpUser, BaseAnalyzerEndpointTest):

    @task
    def predict(self):
        self.client.post(self.analyzer_endpoint_base_url, data=self.valid_json_content, headers=self.valid_headers)

    def on_stop(self):
        stop_server()
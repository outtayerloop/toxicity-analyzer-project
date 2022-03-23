from locust import HttpUser, task
from tests.BasePredictionEndpointTest import BasePredictionEndpointTest
from tests.ServerThread import start_server, stop_server

# Start the server before the tests begin
start_server()


class PredictionEndpointUser(HttpUser, BasePredictionEndpointTest):

    @task
    def predict(self):
        self.client.post(self.prediction_model_endpoint_base_url, data=self.valid_json_content, headers=self.valid_headers)

    def on_stop(self):
        stop_server()
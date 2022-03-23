from flask import Flask, Response
from flask_cors import CORS
from dotenv import load_dotenv
from prometheus_client import start_http_server
from routes.analyzer_route import app_analyzer
from routes.e2e_route import app_e2e
from routes.metrics_route import app_metrics
from services import constants_service as ct


# Take environment variables from .env file
load_dotenv()

# Create the Flask app
app = Flask(__name__)

# Add CORS handling
cors = CORS(app)

# Log the server's activity
app.debug = True

# Register the routes
app.register_blueprint(app_analyzer, url_prefix=f'/{ct.get_analyzer_endpoint_url_prefix()}')
app.register_blueprint(app_e2e, url_prefix='/')
app.register_blueprint(app_metrics, url_prefix=f'/{ct.get_metrics_endpoint_url_prefix()}')


# Start the local Prometheus HTTP server
start_http_server(ct.get_local_prometheus_server_port())


@app.after_request
def set_response_headers(response: Response) -> Response:
    """
    Handle the application's CORS policy
    :param response: response returned to a client
    :return: the response with access control headers
    """
    response.headers.remove('Access-Control-Allow-Origin')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST')
    return response
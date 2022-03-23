from flask import Blueprint, Response
from prometheus_client import multiprocess, generate_latest, CollectorRegistry, CONTENT_TYPE_LATEST
from services.monitoring import METRICS_REQUESTS


# Create the metrics route
app_metrics = Blueprint('metrics', __name__)


@app_metrics.route('', methods=['GET'])
def metrics() -> Response:
    """
    Return the application's metrics from the local Prometheus server.
    """
    METRICS_REQUESTS.labels('toxicity-analyzer-back').inc()
    registry = CollectorRegistry()
    multiprocess.MultiProcessCollector(registry)
    return Response(generate_latest(registry), mimetype=CONTENT_TYPE_LATEST)
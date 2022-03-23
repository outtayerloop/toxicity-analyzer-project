from prometheus_client import Counter, Summary, Gauge, Histogram


# Prediction endpoint total requests counter
REQUESTS = Counter('prediction_requests_total', 'Predictions requested.')

# Metrics endpoint request counter
METRICS_REQUESTS = Counter('metrics_total', 'Metrics requested.', ['app_name'])

# Prediction endpoint exception counter
EXCEPTIONS = Counter('prediction_requests_exceptions_total', 'Exceptions serving predictions.')

# Metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Prediction endpoint in-progress requests counter
IN_PROGRESS = Gauge('prediction_requests_in_progress', 'Number of prediction requests in progress.')

# Prediction endpoint last served prediction request timestamp
LAST = Gauge('prediction_request_last_time_seconds', 'The last time a prediction request was served.')

# Prediction request latency
LATENCY = Summary('prediction_request_latency_seconds', 'Prediction request latency.')

# Prediction request latency histogram
HISTOGRAM_LATENCY = Histogram('prediction_request_histogram_latency_seconds',
                              'Prediction request latency histogram.',
                              buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1])
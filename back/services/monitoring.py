from prometheus_client import Counter, Summary, Gauge, Histogram


# Analyzer endpoint total requests counter
REQUESTS = Counter('analyzer_requests_total', 'Analysis requested.')

# Metrics endpoint request counter
METRICS_REQUESTS = Counter('metrics_total', 'Metrics requested.', ['app_name'])

# Analyzer endpoint exception counter
EXCEPTIONS = Counter('analyzer_requests_exceptions_total', 'Exceptions serving analysis.')

# Metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Analyzer endpoint in-progress requests counter
IN_PROGRESS = Gauge('analyzer_requests_in_progress', 'Number of analyzer requests in progress.')

# Analyzer endpoint last served analysis request timestamp
LAST = Gauge('analyzer_request_last_time_seconds', 'The last time an analyzer request was served.')

# Analyzer request latency
LATENCY = Summary('analyzer_request_latency_seconds', 'Analyzer request latency.')

# Analyzer request latency histogram
HISTOGRAM_LATENCY = Histogram('analyzer_request_histogram_latency_seconds',
                              'Analyzer request latency histogram.',
                              buckets=[0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1])
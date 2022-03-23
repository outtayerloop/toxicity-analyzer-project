const Counter = require('prom-client').Counter
const Summary = require('prom-client').Summary
const Gauge = require('prom-client').Gauge
const Histogram = require('prom-client').Histogram
const Registry = require('prom-client').Registry


module.exports = {
    /**
     * Home page endpoint total requests counter
     */
    REQUESTS : new Counter({
        name: `home_page_requests_total`, 
        help: `Home page navigation requested.`
    }),
    /**
     * Metrics endpoint request counter
     */
    METRICS_REQUESTS : new Counter({
        name: `metrics_total`, 
        help: `Metrics requested.`, 
        labelNames: [`app_name`]
        
    }),
    /**
     *  Home page endpoint exception counter
     */
    EXCEPTIONS : new Counter({
        name: `home_page_requests_exceptions_total`, 
        help: `Exceptions serving home page.`
    }),
    /**
     * Metric to track time spent and requests made.
     */
    REQUEST_TIME : new Summary({
        name: `request_processing_seconds`, 
        help: `Time spent processing request`
    }),
    /**
     *  Home page endpoint in-progress requests counter
     */
    IN_PROGRESS : new Gauge({
        name: `home_page_requests_in_progress`, 
        help: `Number of home page navigation requests in progress.`
    }),
    /**
     *  Home page endpoint last served home page navigation request timestamp
     */
    LAST : new Gauge({
        name: `home_page_request_last_time_seconds`, 
        help: `The last time a home page navigation request was served.`
    }),
    /**
     * Home page navigation request latency
     */
    LATENCY : new Summary({
        name: `home_page_request_latency_seconds`,
        help: `Home page navigation request latency.`
    }),
    /**
     * Home page navigation request latency histogram
     */
    HISTOGRAM_LATENCY : new Histogram({
        name: `home_page_request_histogram_latency_seconds`,
        help: `Home page navigation request latency histogram.`,
        buckets: [0.0001, 0.0002, 0.0005, 0.001, 0.01, 0.1]
    }),
    /**
     * Metrics registry
     */
    registry : new Registry()
}

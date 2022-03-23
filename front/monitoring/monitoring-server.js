const express = require('express')
const config = require('../config')
const service = require('./monitoring-service')
const cors = require('cors')
const bodyParser = require('body-parser')

const app = express()

app.use(cors({
  'origin': '*',
  'methods': "GET,POST,HEAD,OPTIONS",
  'preflightContinue': true,
  'optionsSuccessStatus': 204
}))

app.use(bodyParser.json())

const HOST = config.MONITORING_SERVER_HOST
const PORT = config.MONITORING_SERVER_PORT

/***
 * Initializes the metrics registry.
*/
const getInitializedRegistry = () => {
    service.registry.registerMetric(service.REQUESTS)
    service.registry.registerMetric(service.METRICS_REQUESTS)
    service.registry.registerMetric(service.EXCEPTIONS)
    service.registry.registerMetric(service.REQUEST_TIME)
    service.registry.registerMetric(service.IN_PROGRESS)
    service.registry.registerMetric(service.LAST)
    service.registry.registerMetric(service.LATENCY)
    service.registry.registerMetric(service.HISTOGRAM_LATENCY)
    return service.registry
}

/***
 * Initialized metrics registry
*/
service.registry = getInitializedRegistry()

app.get('/metrics', async (req, res) => {
  res.setHeader(`Content-Type`, service.registry.contentType)
  res.end(await service.registry.metrics())
})

app.get('/beforemount/', async (req, res) => {
  service.REQUESTS.inc()
  service.IN_PROGRESS.inc()
  res.send(`ok`)
})

app.post('/mounted/', async (req, res) => {
  const start = req.body.start
  service.LAST.set(Date.now() / 1000)
  service.IN_PROGRESS.dec()
  service.LATENCY.observe(Date.now() / 1000 - start)
  service.HISTOGRAM_LATENCY.observe(Date.now() / 1000 - start)
  res.send(`ok`)
})

app.listen(PORT, HOST, () => {
    console.log(`Running on http://${HOST}:${PORT}`)
})
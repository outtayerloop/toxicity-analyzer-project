const config = require('./config')

module.exports = {
  devServer: {
    proxy: {
      '/metrics': {
        target: `http://${config.DEV_SERVER_HOST}:${config.MONITORING_SERVER_PORT}`
      }
    }
  }
}
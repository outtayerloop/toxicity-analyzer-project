<template>
  <div style="cursor: default;">

    <nav class="navbar">
        <a id="txt-navbar" class="navbar-brand" style="cursor: default; text-decoration: none; color: rgb(242, 242, 242)">Toxicity analyzer</a>
    </nav>

    <div class="body">
      <div class="center-vertical">
        <div class="form-group w-50 center-horizontal">
          <p id="msg" class="lead">Write a sentence</p>
          <textarea type="sentence" class="form-control control-label" id="sentence" maxlength="500"></textarea>
          
          <br/> 

          <p id="error-message">Invalid input</p>
        
          <div class="pull-right" style="display: flex; flex-direction: row; align-items: center;">
              <button id="submit-btn" type="submit" class="btn btn-dark" style="display: flex; flex-direction: row; align-items: center; justify-content: center; min-width: 83px; min-height: 46px;">
                <span id="progress" aria-hidden="true" class="spinner-border text-light"></span>
                <span id="submit-btn-text">Analyze</span>
              </button>
          </div>

          <br/>  

          <div id="result-msg" style="margin-bottom: 20px">The results are :</div>

          <div id="result" class="lead result" style="display: flex; flex-direction: row; align-items: center; font-size: 1rem;"></div>
          <br/>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const config = require('../../config')
import axios from "axios"

let start = null

/***
 * Updates the metrics which monitor the "beforeMount" hook.
*/
const updateBeforeMountMetrics = () => {
  start = Date.now() / 1000
  axios.get(`http://127.0.0.1:${config.MONITORING_SERVER_PORT}/beforemount/`)
}

/***
 * Updates the metrics which monitor the "mounted" hook.
*/
const updateMountedMetrics = () => {
  axios.post(`http://127.0.0.1:${config.MONITORING_SERVER_PORT}/mounted/`,
              JSON.stringify({'start': start}),
              { headers: { 'content-Type': `application/json` } }
  )
}

export default {
  name: `app`,
  beforeMount: function(){
    updateBeforeMountMetrics()
  },
  mounted: function () {
    updateMountedMetrics()
    this.toggleErrorMessage(false)
    this.toggleSubmitButton(false)
    this.toggleLoadingProgress(false, true)
    this.bindKeyDownEventListenerToTextInput()
    this.bindOnClickEventListenerToSubmitButton()
  },
  methods: {
    /***
      * Shows or hides the error message from the provided visibility.
      * @param visibility the visibility of the error message : boolean true or false
   */
    toggleErrorMessage(visibility) {
      const errorMessage = document.getElementById(`error-message`)
      errorMessage.style.opacity = visibility ? `1` : `0`
    },
    /***
      * Enables or disables the submit button from the provided enabled state value.
      * @param enabled the enabled state of the submit button : boolean true or false
   */
    toggleSubmitButton(enabled) {
      const submitButton = document.getElementById(`submit-btn`)
      submitButton.disabled = !enabled
    },
    /***
      * Shows or hides the progress spinner from the provided visibility and 
      * manages the submit button text and enabled state accordingly.
      * @param visibility the visibility of the progress spinner : boolean true or false
      * @param onMounted determines whether this function is called in the mounted() stage : boolean true or false
   */
    toggleLoadingProgress(visibility, onMounted) {
      const progressSpinner = document.getElementById(`progress`)
      const submitButtonText = document.getElementById(`submit-btn-text`)
      progressSpinner.style.display = visibility ? `initial` : `none`
      submitButtonText.style.display = visibility ? `none` : `initial`
      if(!onMounted)
        this.toggleSubmitButton(!visibility)
    },
    /***
     * Triggered when the input submit button is clicked.
     * Makes a toxicity analysis request to the API endpoint and
     * fills the result zone with the response if it's a 200 OK,
     * else shows the hidden error message.
   */
    onSubmittedInput() {
      if (!this.hasInvalidInput()){
        this.clearResultArea()
        this.toggleLoadingProgress(true, false)
        this.sendToxicityAnalysisRequest()
      }
    },
    /***
     * Sends a request to the toxicity analysis endpoint and updates the UI accordingly.
    */
    sendToxicityAnalysisRequest() {
        const that = this
        const analyzerRequestMetaData = this.getAnalyzerRequestMetaData()
        axios.post(analyzerRequestMetaData.analyzerEndpointUrl, 
                   analyzerRequestMetaData.userInputJson, 
                   analyzerRequestMetaData.options
        )
        .then(res => that.handleToxicityAnalysisRequestSuccess(res))
        .catch(err => that.handleToxicityAnalysisRequestError(err))
    },
    /***
     * Removes all child nodes from the result area.
     */
    clearResultArea(){
      const resultZone = document.getElementById(`result`)
      resultZone.innerHTML = ``
    },
    /***
     * Displays the extracted toxicity statistics in the appropriate zone of the UI.
     * @param res toxicity analysis API endpoint axios-wrapped response
    */
    handleToxicityAnalysisRequestSuccess(res) {
      this.toggleLoadingProgress(false, false)
      const resultZone = document.getElementById(`result`)
      const statisticsContainerNode = document.createElement(`UL`)
      const statistics = res.data.content
      this.appendStatisticsComponent(statistics.identity_attack, `Identity attack`, statisticsContainerNode)
      this.appendStatisticsComponent(statistics.insult, `Insult`, statisticsContainerNode)
      this.appendStatisticsComponent(statistics.obscene, `Obscenity`, statisticsContainerNode)
      this.appendStatisticsComponent(statistics.severe_toxicity, `Severe toxicity`, statisticsContainerNode)
      this.appendStatisticsComponent(statistics.threat, `Threat`, statisticsContainerNode)
      this.appendStatisticsComponent(statistics.toxicity, `Toxicity`, statisticsContainerNode)
      statisticsContainerNode.style.textAlign = `start`
      statisticsContainerNode.style.lineHeight = 1.8
      resultZone.appendChild(statisticsContainerNode)
    },
    /***
     *
     * @param statisticsComponent Statistics component value obtained from the endpoint JSON response
     * @param label Statistics component label
     * @param rootNode Node to which we want to append a new LI node containing the statistics component data
     */
    appendStatisticsComponent(statisticsComponent, label, rootNode){
      const listNode = document.createElement(`LI`)
      const statisticsComponentPercentage = parseFloat(statisticsComponent) * 100
      const nodeText = document.createTextNode(`${label} : ${statisticsComponentPercentage.toFixed(2)} %`)
      listNode.appendChild(nodeText)
      rootNode.appendChild(listNode)
    },
    /***
     * Shows the invalid input error message if response status is 400,
     * else shows a pop up with the error message.
     * @param err Error thrown
    */
    handleToxicityAnalysisRequestError(err) {
      this.toggleLoadingProgress(false, false)
      if (this.hasReceivedServerErrorResponse(err))
          alert(err.response.data.message)
      else
          alert(err.message)
    },
    /***
     * Return the toxicity analysis request's full URL, POST data and options (headers).
     * @returns {{options: {headers: {"content-Type": string}}, analyzerEndpointUrl: string, userInputJson: string}}
     * The above mentioned meta data
     */
    getAnalyzerRequestMetaData() {
      const analyzerEndpointUrl = `${config.API_BASE_URL}/analyzer`
      const inputValue = document.getElementById(`sentence`).value
      const userInputJson = JSON.stringify({'input': inputValue})
      const applicationContentType = `application/json`
      const options = {headers: {'content-Type': applicationContentType}}
      return {
        analyzerEndpointUrl: analyzerEndpointUrl,
        userInputJson: userInputJson,
        options: options
      }
    },
    /***
     * Determine whether the input text value is valid or not.
     * @returns {boolean} true if the input value is null or empty, false otherwise
    */
    hasInvalidInput() {
      const inputValue = document.getElementById(`sentence`).value
      return inputValue === null || inputValue.replace(` `, ``) === ``
    },
    /***
     * Binds an event listener for the keydown event on the text input element.
     * It is used to hide or display the error message if the input respectively
     * contains or not some text.
     * The key code used is taken from this MDN documentation web page :
     * https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/code/code_values
    */
    bindKeyDownEventListenerToTextInput() {
      const textInput = document.getElementById(`sentence`)
      textInput.addEventListener(`keyup`, e => {
          if (e.code === `Backspace` && this.hasInvalidInput()){
            this.toggleErrorMessage(true)
            this.toggleSubmitButton(false)
          }
          else{
            this.toggleErrorMessage(false)
            this.toggleSubmitButton(true)
          }
      })
    },
    /***
     * Binds an event listener for the click event on the submit button element.
    */
    bindOnClickEventListenerToSubmitButton() {
      const submitButton = document.getElementById(`submit-btn`)
      const that = this
      submitButton.addEventListener(`click`, () => that.onSubmittedInput())
    },
    /**
     * Return true if the error contains a response, else return false.
     * @param err received error
     * @returns {boolean}
     */
    hasReceivedServerErrorResponse(err) {
      return (
        err.response !== undefined &&
        err.response !== null &&
        err.response !== false
      );
    }
  }
}
</script>

<style>

.body, html{
  padding: 0;
  margin: 0;
  min-height: 80vh;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #EEEEEE;
  background-color:#242424 ;
}

.navbar{
  margin:0;
  padding:0;
  top:0%;
  width: 100%;
  padding-bottom: 1em;
  background: #343A40;
  color: #EEEEEE;
}

.navbar a {
  float: left;
  display: block;
  color: #f2f2f2;
  text-align: center;
  padding: 15px;
  text-decoration: none;
}

.center-horizontal {
    margin: auto;
    height: 50%;
    padding: 10px;
    text-align: left;
}

.center-vertical{
    margin: auto;
    height: 50%;
    padding: 10px;
}

.result{
  background-color:#343A40 ;
  height:200px; 
  overflow:auto;
  text-align: center;
}


#error-message{
    color: #dc3545;
}

</style>

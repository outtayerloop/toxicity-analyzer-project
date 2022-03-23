def get_prediction_endpoint_url_prefix() -> str:
    """
    Return the model endpoint url prefix
    :return: the model endpoint url prefix
    """
    return 'predict'


def get_metrics_endpoint_url_prefix() -> str:
    """
    Return the metrics endpoint url prefix
    :return: the metrics endpoint url prefix
    """
    return 'metrics'


def get_prediction_endpoint_key() -> str:
    """
    Return the accepted input key of the prediction endpoint
    :return: the accepted input key of the prediction endpoint
    """
    return 'input'


def get_max_input_length() -> int:
    """
    Return the max accepted length for an input from which the endpoint will return a prediction.
    :return: an int containing the value 500
    """
    return 500


def get_none_json_request_body_message() -> str:
    """
    Return the message associated with a missing content type headers 400 Bad Request response
    or None request body JSON.
    :return: the above described message
    """
    return 'Missing application/json content type in request headers or None request body JSON'


def get_missing_input_key_message() -> str:
    """
    Return the message associated with a missing input key 400 Bad Request response
    :return: the above described message
    """
    input_key = get_prediction_endpoint_key()
    return f'POST request JSON body key "{input_key}" not found'


def get_none_input_key_message() -> str:
    """
    Return the message associated with a None input key 400 Bad Request response
    :return: the above described message
    """
    input_key = get_prediction_endpoint_key()
    return f'POST request JSON body "{input_key}" value is null'


def get_too_big_input_length_message() -> str:
    """
    Return the message associated with a too big input length 400 Bad Request response
    :return: the above described message
    """
    max_input_length = str(get_max_input_length())
    return f'Input text too big (max {max_input_length} characters)'


def get_bad_provided_validity_exception_message() -> str:
    """
    Return the exception message returned when a bad validity was provided.
    :return: the exception message returned when a bad validity was provided
    """
    return 'An incorrect validity value was provided.'


def get_ok_response_message() -> str:
    """
    Return the value of the message associated with a 200 OK Flask Response.
    :return: the value of the message
    """
    return 'ok'


def get_response_message_key() -> str:
    """
    Return the response message key associated with any Flask Response.
    :return: the response message key
    """
    return 'message'


def get_response_content_key() -> str:
    """
    Return the response content key associated with any Flask Response.
    :return: the response message key
    """
    return 'content'


def get_prediction_model_host_env_variable_label() -> str:
    """
    Return the label of the prediction model host environment variable used by the api.
    :return: the label of the prediction model host environment variable used by the api.
    """
    return 'PREDICTION_MODEL_HOST'


def get_prediction_model_port_env_variable_label() -> str:
    """
    Return the label of the prediction model port environment variable used by the api.
    :return: the label of the prediction model port environment variable used by the api.
    """
    return 'PREDICTION_MODEL_PORT'


def get_application_content_type() -> str:
    """
    Return the application accepted content type
    :return: the application accepted content type
    """
    return 'application/json'


def get_component_threshold() -> float:
    """
    Return the percentage from which an input is labeled as any of the extracted metrics
    :return: the percentage from which an input is labeled as any of the extracted metrics
    """
    return 0.5


def get_toxicity_label() -> str:
    """
    Return the toxicity label used in the statistics extraction performed in the prediction endpoint
    :return: the toxicity label returned in the dict of the prediction endpoint
    """
    return 'toxicity'


def get_insult_label() -> str:
    """
    Return the insult label used in the statistics extraction performed in the prediction endpoint
    :return: the insult label returned in the dict of the prediction endpoint
    """
    return 'insult'


def get_obscenity_label() -> str:
    """
    Return the obscenity label used in the statistics extraction performed in the prediction endpoint
    :return: the obscenity label returned in the dict of the prediction endpoint
    """
    return 'obscene'


def get_threat_label() -> str:
    """
    Return the threat rate label used in the statistics extraction performed in the prediction endpoint
    :return: the threat rate label returned in the dict of the prediction endpoint
    """
    return 'threat'


def get_identity_attack_label() -> str:
    """
    Return the identity attack label used in the statistics extraction performed in the prediction endpoint
    :return: the identity attack label returned in the dict of the prediction endpoint
    """
    return 'identity_attack'


def get_local_prometheus_server_port() -> int:
    """
    Return the local Prometheus server port
    :return: the local Prometheus server port
    """
    return 8010
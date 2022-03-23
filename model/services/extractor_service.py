from detoxify import Detoxify


# Initialized here so that the model is loaded only once when the server is launched
model = Detoxify('original-small')


def get_toxicity_stats(user_input: str) -> dict[str, str]:
    """
    Return a dict containing the extracted toxicity statistics from the input text.
    It uses the 'original-small' model as it is the lightweight version
    of the original model with the best 'Detoxify score'.
    :param user_input: provided input text
    :return: the extracted toxicity statistics with a two-decimals precision
    """
    toxicity_stats = model.predict(user_input)
    return {
        label: f'{percentage:.4f}'
        for label, percentage in toxicity_stats.items()
    }
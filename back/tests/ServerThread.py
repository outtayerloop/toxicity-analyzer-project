from dotenv import load_dotenv
import os
from services import constants_service as ct
from app import app
from threading import Thread
from werkzeug.serving import make_server


# Take environment variables from .env file
load_dotenv()

# Analyzer endpoint host environment variable
host = os.getenv(ct.get_analyzer_endpoint_host_env_variable_label())

# Analyzer endpoint port environment variable
port = int(os.getenv(ct.get_analyzer_endpoint_port_env_variable_label()))


class ServerThread(Thread):

    def __init__(self, app):
        """
        Initialize a new thread which will contain a Flask server instance.
        :param app: Flask server instance
        """
        Thread.__init__(self)
        self.server = make_server(host, port, app)
        self.ctx = app.app_context()
        self.ctx.push()

    def run(self):
        """
        Start the server.
        """
        self.server.serve_forever()

    def shutdown(self):
        """
        Shut down the server.
        """
        self.server.shutdown()


def start_server():
    """
    Start the server.
    """
    global server
    server = ServerThread(app)
    server.start()


def stop_server():
    """
    Shut down the server.
    """
    global server
    server.shutdown()
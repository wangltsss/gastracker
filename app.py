from log_config import get_logger
from flask import Flask

logger = get_logger(__name__)


app = Flask(__name__)

@app.route("/gastracker")
def hello_world():
    return "<p>Hello, World!</p>"
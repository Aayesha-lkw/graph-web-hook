import os
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def health():
    return "Here App is running."


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )
#!/usr/bin/python3
"""
starts a flask application
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """
    returns homepage
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb_page():
    """
    returns hbnb page
    """
    return render_template("100-hbnb.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

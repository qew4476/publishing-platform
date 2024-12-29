"""Main"""

import os
from flask import Flask, session


app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)


@app.route("/set_session")
def set_session():
    """set the session"""
    session["username"] = "John98"
    # Avoid storing sensitive information like passwords in the session
    session["user_id"] = 1  # Example of storing a user ID instead
    return "set session!"


@app.route("/delete_session")
def delete_session():
    """delete the session"""
    print(session)
    session.pop("username", None)
    print(session)
    return "Session deleted"


@app.route("/", methods=["GET"])
def hello_world():
    """for hellow world"""
    return "<p>Hello World!</p>"


if __name__ == "__main__":
    app.run()

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    return "<p>sdsd, dss! dsd!</p>"

if __name__ == "__main__":
    app.run()
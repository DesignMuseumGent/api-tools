from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/openinghours")
def openinghours():
    # https://schema.org/openingHours
    response = {"openingHours": ["Mo-Fr 10:00-19:00", "Sa 10:00-22:00", "Su 10:00-21:00"]}
    return response

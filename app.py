from flask import Flask
from datetime import date
from utils.utils import open_now
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/openinghours")
def openinghours():
    # https://schema.org/openingHours
    # https://developers.google.com/maps/documentation/places/web-service/details
    # https://www.designmuseumgent.be/bezoek

    today = date.today()

    response = {
        "today": today,
        "open_now": open_now()
    }
    return response

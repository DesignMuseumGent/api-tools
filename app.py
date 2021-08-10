from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/openinghours")
def openinghours():
    # https://schema.org/openingHours
    # https://developers.google.com/maps/documentation/places/web-service/details
    # https://www.designmuseumgent.be/bezoek
    response = {
        "today": date.today(),
        "open_now": True,
        "openingHours": ["Mo-Tu 09:30-17:30", "Th-Fr 09:30-17:30", "Sa-Su 10:00-18:00"]
    }
    return response

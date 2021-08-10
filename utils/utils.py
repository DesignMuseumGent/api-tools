from bs4 import BeautifulSoup
import requests
import json
from datetime import date
import datetime

with open("data/openinghours.json") as f:
    data = json.load(f)


def scrape_opening_hours():
    """"scrape opening hours from https://www.designmuseumgent.be/bezoek"""
    r = requests.get("https://www.designmuseumgent.be/bezoek")
    data = r.text
    return data

def open_now():
    time = date.today().strftime('%A')
    for day in data["openingHoursSpecification"]:
        if time in day["dayOfWeek"]:
            now = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-7]
            if (now >= day["opens"]) and (now < day["closes"]): # groter of gelijk dan opens && kleiner dan closed
                print("open")
                return True
            else:
                return False
                print("c")



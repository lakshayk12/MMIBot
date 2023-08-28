from bs4 import BeautifulSoup
import requests
from alert import Alert


class Bot:

    def __init__(self, url, client_email):
        self.url = url
        self.client_email = client_email

    def check_market_mood(self):
        # Send an HTTP GET request to the webpage
        response = requests.get(self.url)

        # Create a BeautifulSoup object with the page content
        soup = BeautifulSoup(response.content, "html.parser")

        try:
            mmi_number = soup.find(class_='number').getText()
            print("Market Mood Index:", mmi_number)
        except:
            print("Try Again!")

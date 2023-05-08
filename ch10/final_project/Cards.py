import requests
import pprint

class Cards:
    def __init__(self,count=2):
        self.url = f'https://deckofcardsapi.com/api/deck/new/draw/?count={count}'
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        return response['cards'][0]['value']
    





import requests

class Kanye:
    def __init__(self):
        self.url = f'https://api.kanye.rest'
    def get(self):
        r = requests.get(self.url)
        response = r.json()
        if response.get('quote'):
            return response['quote']
        else:
            return None
        

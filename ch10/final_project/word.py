import requests

class RandomWordsAPI:
    def __init__(self):
        self.url = f'https://random-words-api.vercel.app/word'
    def get(self):
        r = requests.get(self.url)
        #response is just a json dictonary of values after .json() call
        response = r.json()
        #check to make sure I got a question, i.e. results
        if response.get('results'):
            return response['results']
        else:
            return None
    def change_category(self, category):
        pass
        #self.url = #...
    
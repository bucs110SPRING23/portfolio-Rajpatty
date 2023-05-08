import requests

class Dad:
    def __init__(self):
        self.url = f'https://icanhazdadjoke.com/'
    def get(self):
        headers = {'Accept': 'application/json'}
        r = requests.get(self.url,headers=headers)
        response = r.json()
        if response.get('joke'):
            return response['joke']
        else:
            return None
import requests

def main():
    response = requests.get("http://icanhazip.com")
    print(response.status_code)
    print(response.text)
main()
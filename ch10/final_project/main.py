import requests
import Cards
import pprint
import Kanye


def main():
    deck = Cards.Cards(count=2)
    results = deck.get()
    yeezy = Kanye.Kanye()
    you = pprint.pprint(results)
    state = True
    

    while state:
        tool = (input("pick number:"))
        if tool == you:
            print(yeezy)
        else:
            print('no')


        
main()
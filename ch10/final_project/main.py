import Cards
import Kanye
import Dad

def main():
    deck = Cards.Cards(count=2)
    results = deck.get()
    yeezy = Kanye.Kanye()
    chicago = yeezy.get()
    father = Dad.Dad()
    man = father.get()
    state = True
    
    while state:
        tool = (str(input("Choose a number or face card (uppercase) from a card deck:")))
        if tool == results:
            print(chicago)
            break
        else:
            print(man)
            break
    print(results)

main()
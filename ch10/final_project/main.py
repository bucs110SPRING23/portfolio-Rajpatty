import Cards
import Kanye
import Dad



def main():
    deck = Cards.Cards(count=2)
    results = deck.get()
    yeezy = Kanye.Kanye()
    acid = yeezy.get()
    state = True
    father = Dad.Dad()
    pops = father.get()
    
    while state:
        tool = (str(input("Choose a number or face card (uppercase) from a card deck:")))
        if tool == results:
            print(acid)
            break
        else:
            print(pops)
            break
    print(results)

main()
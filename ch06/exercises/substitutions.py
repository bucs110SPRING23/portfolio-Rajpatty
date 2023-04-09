import json

def main():
    text = open("ch06/exercises/news.txt","r").read().lower()
    sub_fptr = open("ch06/exercises/subs.json","r")
    subs = json.load(sub_fptr)

    print(subs,type(subs))

    for k,v in subs.items():
        text = text.replace(k,v)

    fptr = open("ch06/exercises/betternews.txt","w")
    fptr.write(text)
    fptr.close()

main()
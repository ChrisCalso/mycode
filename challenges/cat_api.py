
#!/usr/bin/env python3

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://cat-fact.herokuapp.com/facts")

    for catfact in r.json()["all"]:
       # print(catfact.get("text"))
       print(catfact["user"]["name"]["first"]+catfact["user"]["name"]["last"]+" Meeeeeeeeeoooooooooowwwwwww....Do you even know your cat facts?")
main()


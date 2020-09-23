#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("http://api.open-notify.org/astros.json")

    # the .json() method will dump a JSON string into Pythonic data structures. COOL!
    # This is much easier than using the urllib.request library
    print(r.json())

    print("\n\n\n")

    print(f"People in space:{r['number']}")
    print(f"{r['people'][0]['name']} on the {r['people'][0]['craft']}")
    print(f"{r['people'][1]['name']} on the {r['people'][1]['craft']}")
    print(f"{r['people'][2]['name']} on the {r['people'][2]['craft']}")
    
    for astronauts in r.json()["name"]:
        print(astronaut.get("text"))
main()



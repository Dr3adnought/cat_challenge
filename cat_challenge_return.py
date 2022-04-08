#!/usr/bin/env python3

import requests

CATFACTS = "https://cat-fact.herokuapp.com/facts"


def main():

    resp = requests.get(CATFACTS).json()

    for cat in resp:
        print(cat)


if __name__ == "__main__":
    main()

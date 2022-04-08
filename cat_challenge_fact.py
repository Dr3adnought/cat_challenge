#!/usr/bin/env python3

import requests

CATFACTS = "https://cat-fact.herokuapp.com/facts"


def main():

    cats = requests.get(CATFACTS).json()

    for cat in cats:
        print(cat.get("text"))


if __name__ == "__main__":
    main()

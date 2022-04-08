#!/usr/bin/env python3

import requests
import random

CATFACTS = "https://cat-fact.herokuapp.com/facts"


def main():

    cats = requests.get(CATFACTS)

    fatcats = cats.json()

    rando = []

    for cat in fatcats:
        rando.append(cat.get("text"))

    print(random.choice(rando))


if __name__ == "__main__":
    main()

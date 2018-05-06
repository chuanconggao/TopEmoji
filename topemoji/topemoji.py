#! /usr/bin/env python3

import os

from topsim import TopSim

datafile = os.path.join(os.path.split(__file__)[0], "emoji.tsv")

data = [line.strip().split('\t') for line in open(datafile)]
datamap = {i: (emoji, text) for i, (emoji, text) in enumerate(data)}

ts = TopSim((text for emoji, text in data), numGrams=3)

def search(query, k=1):
    return [
        (
            sim,
            [datamap[ln] for ln in lns]
        )
        for sim, lns in ts.search(query, k=k, simFunc="tversky")
    ]

#! /usr/bin/env python3

import os

from topsim import TopSim

datafile = os.path.join(os.path.split(__file__)[0], "emoji.tsv")

data = dict(line.strip().split('\t') for line in open(datafile))
datamap = dict(enumerate(data.items()))

ts = TopSim(data.values(), numGrams=3)

def search(query, k=1):
    return [
        (
            sim,
            [datamap[ln] for ln in lns]
        )
        for sim, lns in ts.search(
            data.get(query, query),
            k=k,
            simFunc="tversky"
        )
    ]

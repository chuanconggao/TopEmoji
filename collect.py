#! /usr/bin/env python3

import re

import requests

r = requests.get("https://unicode.org/Public/emoji/11.0/emoji-test.txt")

parser = re.compile(r"^(\w+(?: \w+)*) +; (\S+) +# (\W+) (.+)$", re.I | re.U)

for l in r.text.split('\n'):
    match = parser.fullmatch(l)
    if match and match.group(2) == "fully-qualified":
        print("{}\t{}".format(match.group(3), match.group(4)))

[![PyPI version](https://img.shields.io/pypi/v/TopEmoji.svg)](https://pypi.python.org/pypi/TopEmoji/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/TopEmoji.svg)](https://pypi.python.org/pypi/TopEmoji/)
[![PyPI license](https://img.shields.io/pypi/l/TopEmoji.svg)](https://pypi.python.org/pypi/TopEmoji/)

🔎 the most similar 😀s in 🐍3️⃣.

- This is an application of [TopSim](https://github.com/chuanconggao/TopSim), which searches the most similar strings against the query in Python 3.

# Installation

This package is available on PyPI. Just use `pip3 install -U TopEmoji` to install it.

# CLI Usage

You can simply use the algorithm on terminal.

``` text
Usage:
    topemoji-cli <query> [-k <k>]
```

- Each emoji and its description and similarity, are printed to terminal and separated by tab character `\t`.

``` bash
topemoji-cli "baby" -k 5
```

``` text
👶	baby	1.0
👼	baby angel	0.666
🐤	baby chick	0.666
🍼	baby bottle	0.6659
🚼	baby symbol	0.6659
```

# API Usage

Alternatively, you can use the algorithm via API.

``` python
from topemoji import search

print(search("face", k=3)) # Return each similarity and the respective emojis.
# [(1.0, [('👶', 'baby')]),
#  (0.6660006660006661, [('👼', 'baby angel'), ('🐤', 'baby chick')]),
#  (0.665889795238888, [('🍼', 'baby bottle'), ('🚼', 'baby symbol')])]
```

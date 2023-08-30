# TrieTree

An implementation of a [Trie Tree](https://en.wikipedia.org/wiki/Trie) in Python.

## Methods

| Header | Information |
|:-------|:------------|
| `__init__(self) -> Self`{.python .highlight} | Initialize a Trie object |
| `insert(self, string: str) -> None`{.python .highlight} | Insert a new `str` to the Trie |
| `remove(self, string: str) -> None`{.python .highlight} | Remove a `str` to the Trie |
| `find(self, string: str) -> FindStatus`{.python .highlight} | Try to find a `str` inside a Trie |
| `__contains__(self, string: str) -> bool`{.python .highlight} | Determine if a `str` is inside a Trie using `in` syntax |
| `__len__(self) -> int`{.python .highlight} | Get the amount of words in a Trie using `len()` syntax |
| `__repr__(self) -> str`{.python .highlight} | Get a `str` representation of the Trie |

### FindStatus

The `find` method returns one of three statuses:

* **FOUND** - the given `str` is a word inserted to the Trie.
* **EXISTS** - the given `str` is present in the Trie as a part of a bigger word.
* **ABSENT** - the given `str` is nor a word in the Trie or a part of another. 


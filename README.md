# TrieTree

An implementation of a [Trie Tree](https://en.wikipedia.org/wiki/Trie) in Python.

## Methods

| Header | Information |
|:-------|:------------|
| `__init__(self) -> None` | Initializes a Trie object. |
| `insert(self, string: str) -> None` | Inserts a new `str` into the Trie. |
| `remove(self, string: str) -> None` | Removes a `str` from the Trie. |
| `find(self, string: str) -> FindStatus` | Tries to find a `str` within the Trie. |
| `__contains__(self, string: str) -> bool` | Determines if a `str` is inside the Trie using the `in` syntax. |
| `__len__(self) -> int` | Gets the count of words in the Trie using the `len()` syntax. |
| `__repr__(self) -> str` | Retrieves a `str` representation of the Trie. |

### FindStatus

The `find` method returns one of three statuses:

* **FOUND** - The given `str` is a word that has been inserted into the Trie.
* **EXISTS** - The given `str` is present in the Trie as part of a larger word.
* **ABSENT** - The given `str` is neither a word in the Trie nor part of another word.

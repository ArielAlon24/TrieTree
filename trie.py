from typing import Optional, Self
from enum import Enum
import string


class FindStatus(Enum):
    FOUND: bool = True
    EXISTS: bool = False
    ABSENT: bool = False


class TrieNode:
    A_ASCII: int = ord("A")
    LETTERS_AMOUNT: int = len(string.ascii_uppercase)

    def __init__(
        self,
        value: Optional[chr] = None,
        is_leaf: bool = False,
    ) -> Self:
        self.value = value
        self.children = [None for _ in range(TrieNode.LETTERS_AMOUNT)]
        self.is_leaf = is_leaf

    def insert(self, string: str, _pointer: int = 0) -> None:
        if _pointer >= len(string):
            return

        char = string[_pointer].upper()
        index = ord(char) - TrieNode.A_ASCII

        if not self.children[index]:
            self.children[index] = TrieNode(value=char)

        if _pointer == len(string) - 1:
            self.children[index].is_leaf = True

        return self.children[index].insert(string=string, _pointer=_pointer + 1)

    def remove(self, string: str, _pointer: int = 0) -> None:
        if _pointer == len(string):
            return

        index = ord(string[_pointer].upper()) - TrieNode.A_ASCII
        child = self.children[index]
        child.remove(string=string, _pointer=_pointer + 1)

        if _pointer == len(string) - 1:
            child.is_leaf = False

        if not any(child.children) and not child.is_leaf:
            self.children[index] = None

    def find(self, string: str, _pointer: int = 0) -> FindStatus:
        if _pointer == len(string):
            return FindStatus.EXISTS

        child = self.children[ord(string[_pointer].upper()) - TrieNode.A_ASCII]

        if not child:
            return FindStatus.ABSENT
        elif _pointer == len(string) - 1 and child.is_leaf:
            return FindStatus.FOUND
        return child.find(string=string, _pointer=_pointer + 1)

    def __repr__(self, _padding: int = 0) -> str:
        if not any(self.children):
            return ""

        index = 1
        result = ""

        for child in self.children:
            if child is not None:
                result += (
                    _padding * "     "
                    + f"({str(index).rjust(2)}) {child.value} {'>' if child.is_leaf else ''}\n"
                )
                result += child.__repr__(_padding=_padding + 1)
                index += 1

        return result


class Trie:
    def __init__(self) -> Self:
        self._root = TrieNode()
        self._word_count = 0

    def insert(self, string: str) -> None:
        self._word_count += 1
        self._root.insert(string)

    def remove(self, string: str) -> None:
        self._word_count -= 1
        self._root.remove(string)

    def find(self, string: str) -> FindStatus:
        return self._root.find(string)

    def __contains__(self, string: str) -> bool:
        return bool(self.find(string).value)

    def __len__(self) -> int:
        return self._word_count

    def __repr__(self) -> str:
        return f"Root\n\n{repr(self._root)}"

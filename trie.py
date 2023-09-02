from typing import Optional, Self, List, Tuple
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

    def insert(self, string: str) -> None:
        node = self

        for pointer in range(len(string)):
            char = string[pointer].upper()
            index = ord(char) - TrieNode.A_ASCII

            if not node.children[index]:
                node.children[index] = TrieNode(value=char)

            node.children[index].is_leaf = pointer == len(string) - 1

            node = node.children[index]

    def remove(self, string: str) -> None:
        stack: List[Tuple[Self, int]] = [(self, 0)]

        while True:
            node, pointer = stack.pop()

            if pointer == len(string):
                break

            index = ord(string[pointer].upper()) - TrieNode.A_ASCII
            child = node.children[index]
            stack.append((child, pointer + 1))

            if pointer == len(string) - 1:
                child.is_leaf = False

            if not any(node.children) and not child.is_leaf:
                node.children[index] = None

    def find(self, string: str) -> FindStatus:
        node = self
        for pointer in range(len(string)):
            node = node.children[ord(string[pointer].upper()) - TrieNode.A_ASCII]
            if not node:
                return FindStatus.ABSENT
            elif pointer == len(string) - 1 and node.is_leaf:
                return FindStatus.FOUND

        return FindStatus.EXISTS

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

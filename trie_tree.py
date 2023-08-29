from typing import Optional, Self
import string


class TrieNode:
    A_ASCII: int = ord("a")
    LETTERS_AMOUNT: int = len(string.ascii_lowercase)

    def __init__(
        self,
        value: Optional[chr] = None,
    ) -> Self:
        self.value = value
        self.children = [None for _ in range(TrieNode.LETTERS_AMOUNT)]

    def insert(self, string: str) -> None:
        if not string:
            return

        char = string[0].lower()
        index = ord(char) - TrieNode.A_ASCII
        if not self.children[index]:
            self.children[index] = TrieNode(value=char)

        return self.children[index].insert(string=string[1:])

    def print(self, padding: int = 0) -> None:
        if not any(self.children):
            return

        count = 0
        for child in self.children:
            if child is not None:
                count += 1
                print(padding * "     " + f"({str(count).zfill(2)}) '{child.value}'")
                child.print(padding + 1)


class TrieTree:
    def __init__(self) -> Self:
        self.root = TrieNode()

    def insert(self, string: str) -> None:
        self.root.insert(str)

    def print(self) -> None:
        self.root.print()

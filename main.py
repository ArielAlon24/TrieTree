from trie import TrieNode


def main() -> None:
    trie = TrieNode()

    trie.insert("to")
    trie.insert("tea")
    trie.insert("ted")
    trie.insert("in")
    trie.insert("int")
    trie.insert("inner")
    trie.insert("hello")

    trie.print()


if __name__ == "__main__":
    main()

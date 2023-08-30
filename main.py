from trie import Trie


def main() -> None:
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")

    print(trie)


if __name__ == "__main__":
    main()

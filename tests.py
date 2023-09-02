import pytest
from trie import Trie, FindStatus


@pytest.fixture
def trie():
    return Trie()


def test_insert(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("app")
    assert len(trie) == 2


def test_insert_multiple(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("banana")
    trie.insert("cherry")
    assert len(trie) == 3


def test_remove(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("app")
    trie.remove("app")
    assert "app" not in trie
    assert len(trie) == 1


def test_remove_last_item(trie: Trie) -> None:
    trie.insert("apple")
    trie.remove("apple")
    assert "apple" not in trie
    assert len(trie) == 0


def test_find_found(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    assert trie.find("app") == FindStatus.FOUND
    assert trie.find("apple") == FindStatus.FOUND
    assert trie.find("banana") == FindStatus.FOUND


def test_find_exsits(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("application")
    assert trie.find("appl") == FindStatus.EXISTS


def test_find_absent(trie: Trie) -> None:
    trie.insert("apple")
    assert trie.find("apples") == FindStatus.ABSENT


def test_contains(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("app")
    assert "apple" in trie
    assert "app" in trie
    assert "banana" not in trie


def test_contains_empty(trie: Trie) -> None:
    assert "apple" not in trie


def test_contains_after_removal(trie: Trie) -> None:
    trie.insert("apple")
    trie.remove("apple")
    assert "apple" not in trie
    assert len(trie) == 0


def test_len(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("app")
    assert len(trie) == 2


def test_repr(trie: Trie) -> None:
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    assert repr(trie) == (
        "Root\n\n"
        "( 1) A \n"
        "     ( 1) P \n"
        "          ( 1) P >\n"
        "               ( 1) L \n"
        "                    ( 1) E >\n"
        "( 2) B \n"
        "     ( 1) A \n"
        "          ( 1) N \n"
        "               ( 1) A \n"
        "                    ( 1) N \n"
        "                         ( 1) A >\n"
    )

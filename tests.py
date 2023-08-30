import pytest
from trie import Trie, FindStatus


@pytest.fixture
def trie():
    return Trie()


def test_insert(trie):
    trie.insert("apple")
    trie.insert("app")
    assert len(trie) == 2


def test_remove(trie):
    trie.insert("apple")
    trie.insert("app")
    trie.remove("app")
    assert "app" not in trie
    assert len(trie) == 1


def test_find(trie):
    trie.insert("apple")
    trie.insert("app")
    trie.insert("banana")
    assert trie.find("app") == FindStatus.FOUND
    assert trie.find("apple") == FindStatus.FOUND
    assert trie.find("banana") == FindStatus.FOUND
    assert trie.find("grape") == FindStatus.ABSENT


def test_contains(trie):
    trie.insert("apple")
    trie.insert("app")
    assert "apple" in trie
    assert "app" in trie
    assert "banana" not in trie


def test_len(trie):
    trie.insert("apple")
    trie.insert("app")
    assert len(trie) == 2

import pytest
from src.trie import Trie

def test_add_string():
    trie = Trie()
    trie.add_string('apple', 5)
    assert trie.strings['apple'] == 5

def test_autocomplete():
    trie = Trie()
    trie.add_string('apple', 5)
    trie.add_string('banana', 3)
    trie.add_string('orange', 4)
    matches = trie.autocomplete('a', limit=10)
    assert matches == ['apple', 'banana', 'orange']

def test_autocomplete_empty_prefix():
    trie = Trie()
    trie.add_string('apple', 5)
    trie.add_string('banana', 3)
    trie.add_string('orange', 4)
    matches = trie.autocomplete('', limit=10)
    assert matches == ['apple', 'banana', 'orange']

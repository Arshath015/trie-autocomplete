# %%
import pydantic
from src.trie import Trie

class String(pydantic.BaseModel):
    value: str
    weight: int

# Create a Trie instance
trie = Trie()

# Add some strings to the Trie
trie.add_string('apple', 5)
trie.add_string('banana', 3)
trie.add_string('orange', 4)

# Get a list of matches for a given prefix
matches = trie.autocomplete('a', limit=10)

# Print the matches
for match in matches:
    print(match)

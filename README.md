# Trie-based Autocomplete with Weighted Ranking
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
One-line pitch: Efficient autocomplete with weighted ranking using Trie data structure
## Table of Contents
* [Overview](#overview)
* [Tech Stack](#tech-stack)
* [Architecture](#architecture)
* [Theoretical Background](#theoretical-background)
* [Installation](#installation)
* [Usage](#usage)
* [API Reference](#api-reference)
* [Research Log](#research-log)
* [Testing](#testing)
* [Limitations](#limitations)
* [Roadmap](#roadmap)
* [License](#license)
## Overview
Implementation of Trie-based autocomplete with weighted ranking for efficient and accurate string matching
## Tech Stack
* Python 3.8+
* Pydantic for data validation
## Architecture
```text
notebooks/
exploration.py
src/
__init__.py
trie.py
weighted_ranker.py
tests/
test_trie.py
results/
findings.md
```
## Theoretical Background
Trie-based autocomplete is an efficient method for string matching. By using a Trie data structure, we can quickly find all strings that match a given prefix. Weighted ranking allows us to prioritize certain matches over others. This is particularly useful when dealing with large datasets where relevance is important.
The time complexity of Trie-based autocomplete is O(m), where m is the length of the input string. This is because we only need to traverse the Trie as far as the input string.
The space complexity of Trie-based autocomplete is O(n), where n is the total number of strings in the dataset. This is because we need to store all strings in the Trie.
In terms of the weighted ranking, we use a simple scoring system where each match is assigned a score based on its relevance. The score is then used to rank the matches.
## Installation
To install the Trie-based autocomplete module, run the following commands:
pip install -r requirements.txt
git clone https://github.com/username/trie-autocomplete.git
## Usage
To use the Trie-based autocomplete module, create an instance of the Trie class and add strings to it using the add_string method. You can then use the autocomplete method to get a list of matches for a given prefix.
## API Reference
* `Trie.add_string(string: str, weight: int)` - Add a string to the Trie with a given weight
* `Trie.autocomplete(prefix: str, limit: int = 10)` - Get a list of matches for a given prefix, limited to the top N matches
## Research Log
See [results/findings.md](results/findings.md) for a written analysis of the research
## Testing
See [tests/test_trie.py](tests/test_trie.py) for unit tests of the Trie-based autocomplete module
## Limitations
The current implementation has some limitations. For example, it does not handle non-ASCII characters. It also does not have a mechanism for updating the weights of existing strings.
## Roadmap
* Add support for non-ASCII characters
* Implement a mechanism for updating the weights of existing strings
* Optimize the scoring system for better performance
## License
MIT License

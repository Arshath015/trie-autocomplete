from collections import defaultdict

class Trie:
    def __init__(self):
        self.root = defaultdict(dict)
        self.strings = {}

    def add_string(self, string: str, weight: int):
        node = self.root
        for char in string:
            if char not in node:
                node[char] = defaultdict(dict)
            node = node[char]
        node['$'] = string
        self.strings[string] = weight

    def autocomplete(self, prefix: str, limit: int = 10):
        node = self.root
        for char in prefix:
            if char not in node:
                return []
            node = node[char]

        matches = self._get_matches(node, prefix)
        matches.sort(key=lambda x: self.strings[x], reverse=True)
        return matches[:limit]

    def _get_matches(self, node, prefix):
        matches = []
        if '$' in node:
            matches.append(node['$'])
        for char, child_node in node.items():
            if char != '$':
                matches.extend(self._get_matches(child_node, prefix + char))
        return matches

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def autocomplete(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        results = []
        self._dfs(node, prefix, results)
        return results

    def _dfs(self, node, current, results):
        if node.is_end:
            results.append(current)
        for ch, child in node.children.items():
            self._dfs(child, current + ch, results)

    def delete(self, word):
        self._delete(self.root, word, 0)

    def _delete(self, node, word, depth):
        if depth == len(word):
            node.is_end = False
            return len(node.children) == 0
        ch = word[depth]
        if ch not in node.children:
            return False
        should_delete = self._delete(node.children[ch], word, depth + 1)
        if should_delete:
            del node.children[ch]
            return not node.is_end and len(node.children) == 0
        return False


# Использование
t = Trie()
for w in ["apple", "app", "application", "apply", "apt", "banana"]:
    t.insert(w)

print(t.search("app"))          # True
print(t.search("appl"))         # False
print(t.starts_with("app"))     # True
print(t.autocomplete("app"))    # ['app', 'apple', 'application', 'apply']
t.delete("app")
print(t.search("app"))          # False
print(t.autocomplete("app"))    # ['apple', 'application', 'apply']
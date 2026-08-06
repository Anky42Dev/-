class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if not node:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        return node

    def search(self, val):
        return self._search(self.root, val)

    def _search(self, node, val):
        if not node:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            # найти inorder successor (минимум правого поддерева)
            successor = node.right
            while successor.left:
                successor = successor.left
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result  # всегда отсортирован

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def min_val(self):
        node = self.root
        while node and node.left:
            node = node.left
        return node.val if node else None

    def max_val(self):
        node = self.root
        while node and node.right:
            node = node.right
        return node.val if node else None

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))


# Использование
bst = BST()
for v in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(v)

print(bst.inorder())    # [20, 30, 40, 50, 60, 70, 80]
print(bst.search(40))   # True
print(bst.min_val())    # 20
print(bst.height())     # 3
bst.delete(30)
print(bst.inorder())    # [20, 40, 50, 60, 70, 80]
class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_val

    def _sift_down(self, i):
        n = len(self.heap)
        smallest = i
        l, r = self.left_child(i), self.right_child(i)

        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r

        if smallest != i:
            self.swap(i, smallest)
            self._sift_down(smallest)

    def peek(self):
        return self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


# Использование
h = MinHeap()
for val in [10, 4, 7, 1, 9, 3]:
    h.insert(val)

print(h)           # [1, 4, 3, 10, 9, 7]
print(h.peek())    # 1
print(h.extract_min())  # 1
print(h)           # [3, 4, 7, 10, 9]
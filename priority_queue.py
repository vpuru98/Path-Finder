
class PriorityQueue:

    @classmethod
    def parent(cls, index):
        return (index - 1) // 2

    @classmethod
    def left_child(cls, index):
        return 2 * index + 1

    @classmethod
    def right_child(cls, index):
        return 2 * index + 2

    def __init__(self, comparator=None):
        self._container = []
        self._comparator = (lambda x, y: x <= y) if comparator == None else comparator

    def _heapify(self, index):
        while True:
            largest = index
            left = self.left_child(index)
            right = self.right_child(index)
            if left < len(self) and not self._comparator(self._container[left], self._container[largest]):
                largest = left
            if right < len(self) and not self._comparator(self._container[right], self._container[largest]):
                largest = right
            if largest == index:
                break
            else:
                temp = self._container[index]
                self._container[index] = self._container[largest]
                self._container[largest] = temp
                index = largest

    def push(self, item):
        self._container.append(item)
        index = len(self) - 1
        while index > 0 and not self._comparator(self._container[index], self._container[self.parent(index)]):
            temp = self._container[index]
            self._container[index] = self._container[self.parent(index)]
            self._container[self.parent(index)] = temp
            index = self.parent(index)

    def pop(self):
        assert len(self) > 0
        item = self._container[0]
        self._container[0] = self._container[len(self) - 1]
        self._container.pop()
        self._heapify(0)
        return item

    def peek(self):
        assert len(self) > 0
        return self._container[0]

    def __len__(self):
        return len(self._container)

    def __str__(self):
        return self._container.__str__()


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.push(3)
    print(pq)
    pq.push(-1)
    print(pq)
    pq.pop()
    print(pq)
    pq.push(4)
    print(pq)
    pq.push(55)
    print(pq)
    pq.push(-44)
    print(pq)
    pq.pop()
    print(pq)
    pq.pop()
    print(pq)
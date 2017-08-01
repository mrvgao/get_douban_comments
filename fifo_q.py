class Queue:
    def __init__(self, length=100):
        self.max_length = length
        self.queue = []

    def push(self, element):
        if self.full():
            self.pop()

        if element not in self.queue:
            self.queue.append(element)

    def pop(self):
        return self.queue.pop(0)

    def full(self):
        return len(self.queue) >= self.max_length

    def __len__(self):
        return len(self.queue)

    def __iter__(self):
        for i in self.queue:
            yield i


if __name__ == '__main__':
    queue = Queue(length=20)

    queue.push(10)
    queue.push(9)

    p = queue.pop()

    assert p == 10

    p = queue.pop()

    assert p == 9

    queue.push(10)
    queue.push(9)

    for i in range(99):
        queue.push(0)

    assert len(queue) == 3

    p = queue.pop()

    assert p == 10

    for i in queue: print(i)

    print('test done!')


class Queue:
    def __init__(self, length=100):
        self.max_length = length
        self.queue = []

    def push(self, element):
        if self.full():
            self.pop()
        self.queue.append(element)

    def pop(self):
        return self.queue.pop(0)

    def full(self):
        return len(self.queue) >= self.max_length


if __name__ == '__main__':
    queue = Queue()

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

    p = queue.pop()

    assert p == 9

    print('test done!')


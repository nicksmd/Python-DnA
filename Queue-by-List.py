class Queue(object):
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.elements = []

    def __len__(self):
        return self.size

    def enqueue(self, e):
        self.elements.append(e)
        self.tail += 1
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return

        res = self.elements[self.head]
        self.head += 1
        return res

    def display(self):
        print 'display queue'
        for x in range(self.head, self.tail):
            print self.elements[x],
        print '\n'


queue = Queue()
queue.display()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print 'dequeue',queue.dequeue()
print 'dequeue',queue.dequeue()
queue.display()
print 'dequeue',queue.dequeue()
queue.display()
class DoubleLinkedQueue(object):
    class _Node:
        def __init__(self, element=None, next_node=None, prev_node=None):
            self._element = element
            self._next = next_node
            self._prev = prev_node

        def get_data(self):
            return self._element

        def get_next(self):
            return self._next

        def get_prev(self):
            return self._prev


    def __init__(self):
        self.size = 0
        self._tail = self._Node()
        self._head = self._tail

    def enqueue(self, element):
        self.size += 1
        self._tail._element = element
        self._tail._next = self._Node()
        tmp = self._tail
        self._tail = self._tail.get_next()
        self._tail._prev = tmp

    def dequeue(self):
        if self.is_empty():
            return None
        res = self._head.get_data()
        self._head.get_next()._prev = None
        self._head = self._head.get_next()
        self.size -= 1
        return res

    def is_empty(self):
        return self.size == 0

    def display(self):
        pointer = self._head
        while pointer.get_data():
            print pointer.get_data(),
            pointer = pointer.get_next()
        print '\n'

queue = DoubleLinkedQueue()
print 'dequeue', queue.dequeue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()
print 'dequeue', queue.dequeue()
queue.display()
print 'dequeue', queue.dequeue()
print 'dequeue', queue.dequeue()
queue.display()
print 'dequeue', queue.dequeue()
queue.display()




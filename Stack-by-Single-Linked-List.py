class LinkedStack(object):
    class _Node:
        __slot__ = '_element', '_next'

        def __init__(self, element=None, next_node=None):
            self._element = element
            self._next = next_node

        def get_data(self):
            return self._element

        def get_next(self):
            return self._next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push_front(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise RuntimeError('Stack is empty')
        return self._head.get_data()

    def push_back(self, e):
        if self.is_empty():
            self._head = self._Node(e)
            self._size += 1
            return

        current_node = self._head
        prev = self._head
        while current_node:
            prev = current_node
            current_node = current_node.get_next()

        prev._next = self._Node(e)
        self._size += 1

    def pop_back(self):
        if self.__len__() == 0:
            return None

        if self.__len__() == 1:
            res = self._head.get_data()
            self._head = self._Node()
            self._size -= 1
            return res

        current_node = self._head
        prev = None
        while current_node.get_next():
            prev = current_node
            current_node = current_node.get_next()

        prev._next = None
        self._size -= 1
        return current_node.get_data()


    def delete(self, e):
        current = self._head
        prev = None
        while current:
            if current.get_data() == e:
                self._size -= 1
                if not prev:
                    self._head = current.get_next()
                else:
                    prev._next = current.get_next()

            prev = current
            current = current.get_next()

    def __str__(self):
        current = self._head
        res = []
        while current:
            res.append(str(current.get_data()))
            current = current.get_next()

        return " ".join(res)

    def value_at(self, index):
        current_index = 0
        current_node = self._head
        if index > self.__len__() - 1:
            raise IndexError("index error")
        while current_index <= index:
            if current_index == index:
                return current_node.get_data()
            else:
                current_index += 1
                current_node = current_node.get_next()


    def n_th_value_from_end(self, index):
        if index > self.__len__() - 1:
            raise IndexError("index error")

        index = self.__len__() - 1 - index
        print index

        return self.value_at(index)

    def reverse(self):
        current_node = self._head
        prev_node = None
        while current_node:
            next_node = current_node.get_next()
            current_node._next = prev_node
            prev_node = current_node
            current_node = next_node

        self._head = prev_node


l = LinkedStack()
l.push_front(10)


print str(l)
print l.pop_back()
print str(l)
# print l.n_th_value_from_end(3)
# print l.value_at(3)






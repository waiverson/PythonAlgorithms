# encoding:utf-8

# Implementation of the stack ADT using a python list
class Stack:
    # creates an empty stack
    def __init__(self):
        self._the_items = list()

    # returns True if the stack is empty or false otherwise
    def isEmpty(self):
        return len(self._the_items) == 0

    # returns the number of items in stack
    def __len__(self):
        return len(self._the_items)

    # returns the top item on the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "cannot peek at an empty stack"
        return self._the_items[-1]

    # removes and returns the top item on the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._the_items.pop()

    # push an item onto the top of the stack
    def push(self, item):
        self._the_items.append(item)


class StackByLink(object):
    #create an empty stack
    def __init__(self):
        self._top = None
        self._size = 0

    # returns true if the stack is empty of false otherwise
    def is_empty(self):
        return self._top is None

    # returns the number of items in stack
    def __len__(self):
        return self._size

    # returns the top item on the stack without removing it
    def peek(self):
        assert not self.is_empty(), "cannot peek at an empty stack"
        return self._top.item

    def pop(self):
        assert not self.is_empty(), "cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1


class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link









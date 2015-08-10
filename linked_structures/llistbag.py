# encoding:utf-8


# Implements the Bag ADT using a singly linked list
class Bag:
    # constructs an empty bag.
    def __init__(self):
        self._head = None
        self._size = 0

    # returns the number of items in the bag
    def __len__(self):
        return self._size

    # Determines if an item is contained in the bag
    def __contains__(self, target):
        cur_node = self._head
        while cur_node is not None and cur_node.item != target:
            cur_node = cur_node.next
        return cur_node is not None

    # Adds a new item to the bag
    def add(self, item):
        new_node = _BagListNode(item)
        new_node.next = self._head
        self._head = new_node
        self._size += 1

    # removes an instance of the item from the bag
    def remove(self, item):
        pred_node = None
        cur_node = self._head
        while cur_node is not None and cur_node.item != item:
            pred_node = cur_node
            cur_node = cur_node.next

        # the item has to be in the bag to remove it
        assert cur_node is not None, "The item must be in the bag"

        # Unlink the node and return the item
        self._size -= 1
        if cur_node is head:
            self._head = cur_node.next
        else:
            pred_node.next = cur_node.next
        return cur_node.item

    # returns an iterator for traversing the list of items
    def __iter__(self):
        return _BagIterator(self._head)

# Defines a private storage class for creating list nodes
class _BagListNode(object):
    def __init__(self, item):
        self.item = item
        self.next = None

# Defines a linked list iterator for the Bag ADT
class _BagIterator:
    def __init__(self, list_head):
        self._cur_node = list_head

    def __iter__(self):
        return self

    def next(self):
        if self._cur_node is None:
            raise StopIteration
        else:
            item = self._cur_node.item
            self._cur_node = self._cur_node.next
            return item






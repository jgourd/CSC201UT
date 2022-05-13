"""
Python utilities used in CSC 201 at UT.
This file includes classes and methods related to the deque.
"""

from CSC201UT.UnorderedList import UnorderedList

class Deque():
    """Defines a deque."""
    def __init__(self):
        self._dq = UnorderedList()

    def add_front(self, item):
        self._dq.append(item)

    def add_rear(self, item):
        self._dq.add(item)

    def remove_front(self):
        return self._dq.pop()

    def remove_rear(self):
        return self._dq.pop(0)

    def is_empty(self):
        return self._dq.is_empty()

    def size(self):
        return self._dq.size()

    def __str__(self):
        return self._dq.__str__()

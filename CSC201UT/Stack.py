"""
Python utilities used in CSC 201 at UT.
This file includes classes and methods related to the stack.
"""

from CSC201UT.UnorderedList import UnorderedList

class Stack:
    """Defines a stack."""
    def __init__(self):
        self._s = UnorderedList()

    def push(self, item):
        self._s.append(item)

    def pop(self):
        return self._s.pop()

    def peek(self):
        if (self._s._tail == None):
            return None
        return self._s._tail._data

    def is_empty(self):
        return self._s.is_empty()

    def size(self):
        return self._s.size()

    def __str__(self):
        return str(self._s)


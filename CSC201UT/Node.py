"""
Python utilities used in CSC 201 at UT.
This file includes classes and methods related to the list node.
"""

class Node:
    """Defines a node."""
    def __init__(self, data):
        self._data = data
        self._link = None

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data

    data = property(get_data, set_data)

    def get_link(self):
        return self._link

    def set_link(self, link):
        self._link = link

    link = property(get_link, set_link)

    def __str__(self):
        return str(self._data)

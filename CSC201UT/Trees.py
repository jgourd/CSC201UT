"""
Python utilities used in CSC 201 at UT.
This file includes classes and methods related to various tree algorithms.
"""

from CSC201UT.Stack import Stack
from CSC201UT.BinaryTree import BinaryTree

def build_tree(expression):
  tokens = expression.split()
  s = Stack()
  t = BinaryTree("")
  s.push(t)
  curr = t

  for token in tokens:
    # the token is (  
    if (token == "("):
      curr.insert_left("")
      s.push(curr)
      curr = curr.left
    elif (token in [ "+", "-", "*", "/" ]):
      curr.value = token
      curr.insert_right("")
      s.push(curr)
      curr = curr.right
    elif (token == ")"):
      curr = s.pop()
    else:
      curr.value = int(token)
      curr = s.pop()

  return t

def evaluate(tree):
  if (tree):
    left = evaluate(tree.left)
    right = evaluate(tree.right)
    if (left and right):
      if (tree.value == "+"):
        return left + right
      elif (tree.value == "-"):
        return left - right
      elif (tree.value == "*"):
        return left * right
      else:
        return left / right
    else:
      return tree.value


#!/usr/bin/python3
"""class Node that defines a node of a singly linked list"""


class Node:
  def __init__(self, data, next_node=None):
    self.__data = data
    self.__next_node = next_node

  @property
  def data(self):
    return self.__data

  @data.setter
  def data(self, value):
    self.__data = value
    if not isinstance(self.__data, int):
      raise TypeError("data must be an integer")

  @property
  def next_node(self):
        return self.__next_node

  @next_node.setter
  def next_node(self, value):
    self.__next_node = value
    if not isinstance(self.__next_node, Node) or self.__next_node == None:
      raise TypeError("next_node must be a Node object")


"""class SinglyLinkedList that defines a singly linked list"""
 class SinglyLinkedList:
   def __init__(self):
     ghj

  def sorted_insert(self, value):

'''
Problem Statement
Given the head of a Singly LinkedList, reverse the LinkedList.
 Write a function to return the new head of the reversed LinkedList.
'''


#answer
from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse(head):
    p1 = None
    p2 = head

    while p2 is not None:
        temp = p2.next

        p2.next = p1
        p1 = p2

        p2 = temp

    return p1

def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

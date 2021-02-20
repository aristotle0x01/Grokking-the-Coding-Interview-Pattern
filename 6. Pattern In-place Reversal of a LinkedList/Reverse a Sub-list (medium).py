'''
Problem Statement
Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.
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

# 1 <= p <= q <= length
def reverse_sub_list(head, p, q):
    if p >= q:
        return head

    # 1 2 3 4 5
    # 2 4

    # locate node before p
    lp = None
    k = p
    while k > 1:
        k = k - 1
        if lp is None:
            lp = head
        else:
            lp = lp.next

    # locate node before q
    k = q - p
    lq = lp
    while k >= 0:
        k = k - 1
        if lq is None:
            lq = head
        else:
            if lq.next is not None:
                lq = lq.next
            else:
                lq = None
                break

    if lp is None:
        sub_head = head
    else:
        sub_head = lp.next

    if lq is None:
        next_sub_head = None
    else:
        next_sub_head = lq.next
        lq.next = None

    temp = sub_head

    sub_head = reverse(sub_head)
    if lp is not None:
        lp.next = sub_head
    else:
        head = sub_head

    temp.next = next_sub_head

    return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 1, 5)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

'''
Problem Challenge 1

Reverse alternating K-element Sub-list (medium)

Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
Output:   3->2->1->4->5->6->9->8->7->NULL.
'''

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


def reverse_alternate_k_sublist(head, k):
    loop = 0
    k_loop_count = 0
    p = head
    reverse_from = head
    r = None
    new_head = None
    previous_tail = None
    while p is not None:
        p = p.next

        loop = loop + 1
        if loop % k == 0:
            k_loop_count = k_loop_count + 1
            if k_loop_count % 2 == 1:
                if k_loop_count == 1:
                    new_head = reverse_k_nodes(reverse_from, k)
                else:
                    r = reverse_k_nodes(reverse_from, k)
                    previous_tail.next = r

            reverse_from = p

            i = 0
            if previous_tail is None:
                previous_tail = new_head
                while i < (k - 1):
                    previous_tail = previous_tail.next
                    i = i + 1
            else:
                while i < k:
                    previous_tail = previous_tail.next
                    i = i + 1

    return new_head


def reverse_k_nodes(head, k):
    if head is None:
        return

    p1 = None
    p2 = head
    i = 0
    while p2 is not None and i < k:
        p = p2.next
        p2.next = p1
        p1 = p2
        p2 = p

        i = i + 1

    head.next = p2

    return p1


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  #head.next.next.next.next.next.next.next = Node(8)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_sublist(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

'''
Problem Challenge 1
Palindrome LinkedList (medium)
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''

'''
Problem Challenge 1
Palindrome LinkedList (medium)
Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.
Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true
Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''

'''
solution1
    遍历链表，将之入于数组，而后对数组进行处理

solution2
    快慢指针
    快指针到尾部时，慢指针走了一半，将后一半倒置，从头开始比对即可
'''

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def is_palindrome_list(head):
    if head is None:
        return False
    if head.next is None:
        return True

    steps_to_compare = 0
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next
        if fast is not None:
            fast = fast.next

        steps_to_compare = steps_to_compare + 1

    half_head = reverse(slow)
    for i in range(steps_to_compare):
        if head.value != half_head.value:
            return False
        head = head.next
        half_head = half_head.next

    return True

def reverse(head):
    p1 = None
    p2 = head
    while p2 is not None:
        temp = p2.next

        p2.next = p1
        p1 = p2

        p2 = temp

    return p1

def is_palindrome_list2(list):
    a = []
    while list is not None:
        a.append(list.value)
        list = list.next

    start = 0
    end = len(a) - 1
    while end >= start:
        if a[end] != a[start]:
            return False

        start = start + 1
        end = end - 1

    return True


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  #print("Is palindrome: " + str(is_palindrome_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindrome_list(head)))


main()

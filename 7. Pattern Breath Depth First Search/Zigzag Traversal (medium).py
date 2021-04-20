'''
Problem Statement

Given a binary tree, populate an array to represent its zigzag level order traversal.
You should populate the values of all nodes of the first level from left to right,
then right to left for the next level and keep alternating in the same manner for the following levels.
'''

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # tree traversal using 'next' pointer
  def print_tree(self):
    print("Traversal using 'next' pointer: ", end='')
    current = self
    while current:
      print(str(current.val) + " ", end='')
      current = current.next


def zigzag_level_traversal(root):
    result = []

    queue = deque()
    queue.append(root)
    while True:
        count = len(queue)
        if count == 0:
            break

        i = 0
        while i < count:
            i += 1
            e = queue.popleft()
            result.append(e.val)
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)

        count = len(queue)
        i = 0
        while i < count:
            i += 1
            e = queue.pop()
            result.append(e.val)
            if e.right:
                queue.appendleft(e.right)
            if e.left:
                queue.appendleft(e.left)

    return result


'''
    Input Tree
           12
          / \
         7   1
        /   / \
       9    10 5 
           / \
          20 17
'''
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(zigzag_level_traversal(root)))


main()

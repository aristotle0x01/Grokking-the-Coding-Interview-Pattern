'''
Problem Statement
Given a binary tree, populate an array to represent its level-by-level traversal.
You should populate the values of all nodes of each level from left to right in separate sub-arrays.
'''


from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def sub_array(root):
    list = []

    queue = deque()
    queue.append(root)
    while queue:
        t = []
        s = []
        while queue:
            node = queue.popleft()
            t.append(node.val)
            s.append(node)

        list.append(t)

        for k in s:
            if k.left is not None:
                queue.append(k.left)
            if k.right is not None:
                queue.append(k.right)

    return list


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = sub_array(root)
  print(result)


main()

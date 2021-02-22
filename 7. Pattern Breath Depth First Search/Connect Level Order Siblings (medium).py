'''
Problem Statement
Given a binary tree, connect each node with its level order successor.
The last node of each level should point to a null node.
'''


from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

def level_next(root):
    list = sub_array(root)

    for x in list:
        if len(x) <= 1:
            continue
        for i, val in enumerate(x):
            if i == len(x) - 1:
                break
            x[i].next = x[i+1]

    return list

def sub_array(root):
    list = []

    queue = deque()
    queue.append(root)
    while queue:
        s = []
        while queue:
            node = queue.popleft()
            s.append(node)

        list.append(s)

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
  result = level_next(root)
  for a in result:
      t = a[0]
      while t is not None:
          print("{} {}".format(" ", t.val), end =" ")
          t = t.next
      print('\n')

main()

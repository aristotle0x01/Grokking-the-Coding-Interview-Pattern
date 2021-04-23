'''
Problem Statement

Given a binary tree and a number ‘S’,
find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

注意分析题意：
    只要是从上到下的路径，任意起止皆可

    那么遍历所有结点，以当前结点为根结点，找出所有加和为s的路径
'''

from collections import deque

class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_all_paths_with_sum_equal_to_s(root, s):
    paths = []

    if root is None:
        return paths

    q = deque()
    q.append(root)
    while q:
        e = q.popleft()
        find_paths_from(e, s, [], paths)

        if e.left is not None:
            q.append(e.left)

        if e.right is not None:
            q.append(e.right)

    return paths

def find_paths_from(root, s, current_path, paths):
    if root is None:
        return

    current_path.append(root.val)

    if root.val == s:
       paths.append(current_path.copy())

    if root.left is not None:
        find_paths_from(root.left, s - root.val, current_path, paths)

    if root.right is not None:
        find_paths_from(root.right, s - root.val, current_path, paths)

    del current_path[len(current_path) - 1]

'''
    Input Tree
           12
          / \
         7   -1
        /   / \
       4    10 0
    -4     1
       4
    
'''
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(-1)
  root.left.left = TreeNode(4)
  root.left.left.left = TreeNode(-4)
  root.left.left.left.right = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.left.left = TreeNode(1)
  root.right.right = TreeNode(0)
  print("Tree has paths: " + str(find_all_paths_with_sum_equal_to_s(root, 11)))


main()

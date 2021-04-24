'''
Problem Challenge 2

Path with Maximum Sum (hard)

Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.
A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.

as how to understand what this problem means
ref: https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

for a binary tree like this:
            1
         /     \
        2      10
       / \    /  \
     -1  -4  -5   -6
         /   / \
        3   7   4
             \
             -2
solution:
from a bottom-up view, each subtree(can be a leaf) will have a local max, as well as a
local max including root of this subtree

up one level, for the parent of this subtree, let's do the math for its left and right subtree,
with root.val, calc its local max, and local max with parent root

after calc, each subtree can be viewed as a single node with its value as local max including root
imagine the tree collapsed

and finally we will get to the root of tree
'''


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_max_path_sum(root):
    with_root_max, local_max = find_inner(root)

    if with_root_max > local_max:
        return with_root_max
    else:
        return local_max


def check_value(v):
    if v is None:
        return 0
    else:
        return v


def find_inner(root):
    # 包含root结点的最大连通加和
    with_root_max = None

    # 不一定包含root结点的最大连通加和
    local_max = None

    if root is None:
        return with_root_max, local_max

    if root.left is None and root.right is None:
        with_root_max, local_max = root.val, root.val
        return with_root_max, local_max

    # recursive
    l_with_root_max, l_local_max = find_inner(root.left)
    r_with_root_max, r_local_max = find_inner(root.right)

    a = []

    # calc max including root for this tree root
    with_root_max = root.val
    a.append(with_root_max)
    a.append(with_root_max + check_value(l_with_root_max))
    a.append(with_root_max + check_value(r_with_root_max))
    a.sort()
    with_root_max = a[-1]

    # calc local max (without root connected possibly)
    a.append(root.val + check_value(r_with_root_max) + check_value(l_with_root_max))
    if l_local_max is not None:
        a.append(l_local_max)
    if r_local_max is not None:
        a.append(r_local_max)
    a.sort()
    local_max = a[-1]

    return with_root_max, local_max
'''
    Input Tree
           12
          / \
         7   -1
'''
def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  print("Maximum Path Sum: " + str(find_max_path_sum(root)))

  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(find_max_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(find_max_path_sum(root)))

  root = TreeNode(10)
  root.left = TreeNode(2)
  root.right = TreeNode(10);
  root.left.left = TreeNode(20);
  root.left.right = TreeNode(1);
  root.right.right = TreeNode(-25);
  root.right.right.left = TreeNode(3);
  root.right.right.right = TreeNode(4);
  print("Maximum Path Sum: " + str(find_max_path_sum(root)))

  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(10)
  root.left.left = TreeNode(-1)
  root.left.right = TreeNode(-4)
  root.right.left = TreeNode(-5)
  root.right.right = TreeNode(-6)
  root.left.right.left = TreeNode(4)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(4)
  root.right.left.left.right = TreeNode(-2)
  print("Maximum Path Sum: " + str(find_max_path_sum(root)))

main()

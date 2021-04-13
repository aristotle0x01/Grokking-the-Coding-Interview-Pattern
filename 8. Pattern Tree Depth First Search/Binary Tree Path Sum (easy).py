'''
Problem Statement
Given a binary tree and a number ‘S’,
find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.
'''


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def path_sum_exist(root, sum):
    if root is None:
        if sum == 0:
            return True
        else:
            return False
    else:
        left = path_sum_exist(root.left, sum - root.val)
        if left is False:
            return path_sum_exist(root.right, sum - root.val)
        return True

    return False


'''
    12
 7         1
9        10 5
'''
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(path_sum_exist(root, 28)))
    print("Tree has path: " + str(path_sum_exist(root, 18)))

main()

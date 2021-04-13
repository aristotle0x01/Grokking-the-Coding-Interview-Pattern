'''
Problem Statement
Given a binary tree and a number ‘S’,
find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
'''

#answer
class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def find_all_paths(root, sum):
    all_paths = []
    find_path_recursively(root, sum, [], all_paths)
    return all_paths

def find_path_recursively(current_node, sum, previous_route, all_paths):
    if current_node is None:
        return None

    previous_route.append(current_node.val)

    if current_node.val == sum and current_node.left is None and current_node.right is None:
        all_paths.append(list(previous_route))
    else:
        find_path_recursively(current_node.left, sum - current_node.val, previous_route, all_paths)
        find_path_recursively(current_node.right, sum - current_node.val, previous_route, all_paths)

    # already used this node(route), delete it
    del previous_route[-1]
'''
    12
 7         1
4        10 5
'''
def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_all_paths(root, sum)))


main()

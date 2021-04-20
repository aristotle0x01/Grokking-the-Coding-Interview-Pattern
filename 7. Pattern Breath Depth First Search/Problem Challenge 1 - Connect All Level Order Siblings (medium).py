'''
Problem Challenge 1

Connect All Level Order Siblings (medium)
Given a binary tree, connect each node with its level order successor.
The last node of each level should point to the first node of the next level.

Input Tree
       A
      / \
     B   C
    / \   \
   D   E   F


Output Tree
       A--->B
      / \
     B-->C-->D
    / \   \
   D-->E-->F-->NULL
'''

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


def connect_level_order_siblings(root):
    current_level = []
    last_node_current_level = None
    child_level = []

    current_level.append(root)
    while True:
        for node in current_level:
            if node.left is not None:
                child_level.append(node.left)
            if node.right is not None:
                child_level.append(node.right)

        # connect last node of last level to first node of current level
        if last_node_current_level is not None:
            last_node_current_level.next = current_level[0]

        for i in range(1, len(current_level)):
            current_level[i-1].next = current_level[i]

        # set current level last node
        last_node_current_level = current_level[len(current_level) - 1]

        current_level.clear()
        current_level.extend(child_level)
        child_level.clear()
        if len(current_level) == 0:
            break

    return


'''
    Input Tree
           12
          / \
         7   1
        /   / \
       9    10 5 
'''
def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)
  root.print_tree()


main()

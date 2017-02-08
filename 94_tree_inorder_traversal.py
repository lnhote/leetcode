# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _inorderTraversal1(self, result, root):
        if root.left != None:
            self._inorderTraversal1(result, root.left)
        result.append(root.val)
        if root.right != None:
            self._inorderTraversal1(result, root.right)

    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._inorderTraversal1(result, root)
        return result

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if isinstance(root, TreeNode) == False:
            return []
        while root != None:
            stack.append(root)
            root = root.left
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right != None:
                node = node.right
                while node != None:
                    stack.append(node)
                    node = node.left
        return result
'''
   1
  /  \
 4    2
    /  \
   3    6
'''
if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(4)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(6)
    print Solution().inorderTraversal(tree)
    print Solution().inorderTraversal1(tree)

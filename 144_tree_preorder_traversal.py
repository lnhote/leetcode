# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _preorderTraversal(self, result, root):
        result.append(root.val)
        if root.left != None:
            self._preorderTraversal(result, root.left)
        if root.right != None:
            self._preorderTraversal(result, root.right)

    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._preorderTraversal(result, root)
        return result

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if isinstance(root, TreeNode) == False:
            return []
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            result.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
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
    print isinstance(tree, TreeNode)
    print isinstance([], TreeNode)
    print Solution().preorderTraversal(tree)

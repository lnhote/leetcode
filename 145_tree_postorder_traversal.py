# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def _postorderTraversal(self, result, root):
        
        if root.left != None:
            self._postorderTraversal(result, root.left)
        if root.right != None:
            self._postorderTraversal(result, root.right)
        result.append(root.val)

    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self._postorderTraversal(result, root)
        return result

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        if isinstance(root, TreeNode) == False:
            return []
        stack.append(root)
        last_node = root
        while len(stack) > 0:
            node = stack[-1]
            if last_node == node.left or last_node == node.right:
                result.append(node.val)
                stack.pop()
            elif node.left == None and node.right == None:
                result.append(node.val)
                stack.pop()
            else:
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
            last_node = node
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
    print Solution().postorderTraversal1(tree)
    print Solution().postorderTraversal(tree)

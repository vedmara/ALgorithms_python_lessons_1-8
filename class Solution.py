class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        
        if not root:
            return []
        stack, result = [root], []
        while stack:
            if root.left:
                stack.append(root.left)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                
                if node.right:
                    stack.append(node.right)
                    root = node.right
        return result
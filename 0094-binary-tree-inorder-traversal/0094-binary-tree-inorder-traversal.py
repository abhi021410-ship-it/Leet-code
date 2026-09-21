class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        result=[]
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
        inorder(root)
        return result
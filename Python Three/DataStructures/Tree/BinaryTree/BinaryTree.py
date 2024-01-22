import BinaryTreeBase
        

class Solution:
    def invertTree(self, root):
        if not root:
            return None 
        print("Root ", root.val, " Left :", root.left.val if root.left else None, " Right :", root.right.val if root.right else None)
       # root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
a=[4,2,7,1,3,6,9]
bt=BinaryTreeBase.create_binary_tree(a)
s=Solution()
k=s.invertTree(bt)
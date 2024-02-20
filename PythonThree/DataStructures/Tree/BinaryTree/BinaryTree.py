from collections import deque
import BinaryTreeBase
        

class Solution:
    def invert_tree_recursively(self, root):
        if not root:
            return None 
        print("Root ", root.val, " Left :", root.left.val if root.left else None, " Right :", root.right.val if root.right else None)
       # root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    def invert_tree_iteratively(self, root):
        if root is None:
            return root 
        dequ=deque([root]) #Pop & Add at first and last is O(1)
        while dequ:
            node=dequ.popleft()
            
            #Swapping 
            node.right,node.left=node.left,node.right
            
            if node.right:
                dequ.append(node.right)
            if node.left:
                dequ.append(node.left)       
    def get_all_paths_iteratively_dfs(self,root):
        '''This function will print all the paths 
        From root to all the leaves using Depth first search'''
        
        if root is None:
            print("Empty tree")
        
        stack=[(root,[])] #(Current_Node,PathfromRoot)
        
        while stack:
            node,path=stack.pop()
            path.append(node.val) #Adding the current val to the path, As it needs to add in all 3 If condition below, added here
            
            if node.right is None and node.left is None:
                #Node having no child, SO it is a leaf node
                print(path)
                
            if node.right:
                #Appending the node with, its path from the root
                #As the path variable changes, we are creating a spertae copy for this node
                stack.append((node.right,path.copy()))
    
            if node.left:
                #Appending the node with, its path from the root
                #As the path variable changes, we are creating a spertae copy for this node
                stack.append((node.left,path.copy()))
    def maxDepth(self, root) -> int:
        if not root:
            return root
        maxHeight=0
        stack=[(root,maxHeight)]
        while stack:
            node,height=stack.pop()
            height+=1
            if node.right is None and node.left is None:
                #leaf node
                maxHeight=max(maxHeight,height)
            if node.right:
                stack.append((node.right,height))
            if node.left:
                stack.append((node.left,height))
        return maxHeight
    def diameterOfBinaryTree(self, root) :
        d={}
        def dfs_postorder(root):
            if root:
                dfs_postorder(root.left)
                dfs_postorder(root.right)

                left_height=d.get(root.left,0)-1
                right_height=d.get(root.left,0)-1

                d[root.val]=left_height+right_height
        print(d)
        return 0
class DepthFirstSearch:
    # <Root> <Left> <Right>
    def dfs_preorder_iteratively(self,root):
        stack=[]
        preorder_result=[]
        while root or stack:
            if root:
                stack.append(root)
                preorder_result.append(root.val)
                root=root.left
            else:
                prev_node=stack.pop()
                root=prev_node.right
        return preorder_result
    
    # <Left> <Root> <Right>
    def dfs_inorder_iteratively(self,root):
        stack=[]
        inorder_result=[]
        while stack or root:
            if root:
                #Adding to the stack and going down left side deeply.
                stack.append(root)
                root=root.left
            else:
                #If it doesn't have anymore left node 
                # 1. Get the parent from the stack As the root will be num since root=root.left or root=prev_node.right
                # 2. Set the root as the right node of that same level
                prev_node=stack.pop()
                inorder_result.append(prev_node.val)
                root=prev_node.right
                
        return inorder_result
    

    # <Left> <Right> <Root>
    def dfs_postorder_iteratively(self,root):
        stack=[]
        
    # <Left> <Right> <Root>
    def dfs_postorder_recursively(self,root):
        if root:
            self.dfs_postorder_recursively(root.left)
            self.dfs_postorder_recursively(root.right)
            print(root.val)
            
    
    
inp=[4,2,7,1,3,6,9]
created_binary_tree=BinaryTreeBase.create_binary_tree(inp)
sol=DepthFirstSearch()
res=sol.dfs_postorder_recursively(created_binary_tree)

if res:
    print(res)
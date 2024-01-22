from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val 
        self.left=left
        self.right=right
def create_binary_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        node = queue.popleft()
        if lst[i] is not None:
            left = TreeNode(lst[i])
            node.left = left
            queue.append(left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            right = TreeNode(lst[i])
            node.right = right
            queue.append(right)
        i += 1
    return root
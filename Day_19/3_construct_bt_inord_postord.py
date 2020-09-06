class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) time and space
def buildTree(inorder, postorder):
    # postorder: left child -> right child -> Node
    # inorder : left child -> Node -> right child
    # last node of postorder is root node

    indices = dict()
    for i, num in enumerate(inorder):
        indices[num] = i
        
    n = len(postorder)
    idx = n - 1
    
    def recurse(l, r):
        nonlocal idx
        if l > r: return None
        
        num = postorder[idx]
        idx -= 1
        node = TreeNode(num)
        
        if l == r: return node
        
        in_idx = indices[num]
        
        # switch the order of recursive calls as you encounter rigth child first (when iterating idx from the back in postorder array)
        node.right = recurse(in_idx + 1, r)
        node.left = recurse(l, in_idx - 1)
        
        return node

    return recurse(0, n-1)
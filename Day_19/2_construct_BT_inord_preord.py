class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(N) time and space
def buildTree(preorder, inorder):
    # preorder: Node -> left child -> right child
    # inorder : left child -> Node -> right child
    # First node of preorder is root node

    indices = dict()
    for i, num in enumerate(inorder):
        indices[num] = i
    
    idx = 0
    def recurse(l, r):
        nonlocal idx
        
        if l > r: return None
        
        num = preorder[idx]
        node = TreeNode(num)
        idx += 1
        
        if l == r: return node
        
        in_idx = indices[num]
        
        node.left = recurse(l, in_idx - 1)
        node.right = recurse(in_idx + 1, r)
        
        return node
    return recurse(0, len(preorder) - 1)
            
        
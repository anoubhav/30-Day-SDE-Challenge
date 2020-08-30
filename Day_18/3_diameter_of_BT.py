class TreeNode:
    def __init__(self, val=0, left=None, right=None, height = None):
        self.val = val
        self.left = left
        self.right = right
        self.height = height

def diameterBT_editorial(root):
    # One pass solution; does not modify the tree node class with attribute height
    ans = 0
    def getHeights(node):
        nonlocal ans
        if not node: return 0
        l = getHeights(node.l)
        r = getHeights(node.r)
        ans = max(ans, l + r)
        return max(l, r) + 1
    
    getHeights(root)
    return ans



def diameterBT_myAttempt(root):
    if not root: return 0

    # Assuming leaf nodes have height 0
    def getHeights(node):
        if not node:
            return 0
        elif not node.left and not node.right: #leaf node
            node.height = 0
        else: # internal node
            node.height = 1 + max(getHeights(node.left), getHeights(node.right))
        return node.height
    
    getHeights(root)

    # For every node using DFS check where left + right height is maximum, that is the diameter
    stack = [root]
    ans = 0
    while stack:
        node = stack.pop()
        lh, rh, extra = 0, 0, 0
        if node.left:
            stack.append(node.left)
            lh = node.left.height
            extra += 1
        if node.right:
            stack.append(node.right)
            rh = node.right.height
            extra += 1
        ans = max(ans, lh + rh + extra)
    return ans

        
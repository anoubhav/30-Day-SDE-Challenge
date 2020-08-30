# Q: https://leetcode.com/problems/balanced-binary-tree/submissions/
def isBalanced(root):
    ans = True
    def getHeights(node):
        nonlocal ans
        if not node: return 0
        l = getHeights(node.left)
        r = getHeights(node.right)
        if abs(l - r) > 1:
            ans = False
        return 1 + max(l, r)
    getHeights(root)
    return ans
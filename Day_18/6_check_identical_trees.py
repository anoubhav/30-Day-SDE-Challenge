# Q: https://leetcode.com/problems/same-tree/

def usingPreOrderTraversal(p, q):
    # Time: O(N), space: O(N)
    def preorder(node):
        return [node.val] + preorder(node.left) + preorder(node.right) if node else [None]
    
    return preorder(p) == preorder(q)

def usingRecursion(p, q):
    # Time: O(N), space: O(N), average case space (balanced tree): O(log N)
    def recurse(p, q):
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and recurse(p.left, q.left) and recurse(p.right, q.right)
    return recurse(p, q)

# Ref: https://leetcode.com/problems/same-tree/solution/356238
def usingIteration(p, q):
    stack = [(p, q)]
    while stack:
        (p, q) = stack.pop()
        if p and q and p.val == q.val:
            stack.extend([
                (p.left,  q.left),
                (p.right, q.right)
            ])
        elif p or q:
            return False
    return True
# Left - Right - Parent
# Q: https://leetcode.com/problems/binary-tree-postorder-traversal/

def recursePostorder(root):
    return recursePostorder(root.left) + recursePostorder(root.right) + root.val if root else []

# Ref: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45582/A-real-Postorder-Traversal-.without-reverse-or-insert-4ms
def iterativePostorder(root):
    traversal = []
    if not root: return traversal
    st = [root] * 2
    while st:
        cur = st.pop()
        if st and st[-1] is cur:
            if cur.right:
                st += [cur.right] * 2
            if cur.left:
                st += [cur.left] * 2
        else:
            traversal.append(cur.val)
    return traversal
        
def iterativeVisited(root):
    # Simplest solution
    stack = [(root, False)]
    traversal = []
    while stack:
        node, visited = stack.pop()
        if node:
            if visited: 
                traversal.append(node.val)
            else:
                # LIFO
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return traversal


def modifiedPreorder(root):
    # Preorder -> Parent --> left --> right. Modify it to Parent --> right --> left and reverse the traversal while output.
    stack, traversal = [root], []
    while stack:
        node = stack.pop()
        if node:
            stack.append(node.left)
            stack.append(node.right)
            traversal.append(node.val)
    return traversal[::-1]
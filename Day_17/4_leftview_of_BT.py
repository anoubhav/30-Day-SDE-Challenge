# Q: https://leetcode.com/problems/binary-tree-right-side-view/ (same as left side view; only change left <-> right in code)

from collections import defaultdict
def rightSideViewIterative(root):
    if not root: return []
    view = []
    stack = [(root, 0)]
    processed = defaultdict(int)
    while stack:
        node, level = stack.pop()
        if processed[level] == 0:
            view.append(node.val)
            processed[level] = 1
            
        if node.left:
            stack.append((node.left, level + 1))
            
        if node.right:
            stack.append((node.right, level + 1))
    return view

def rightSideViewRecursive(root):
    def recurse(node, level):
        if node:
            if level == len(view):
                view.append(node.val)
            recurse(node.right, level + 1)
            recurse(node.left, level + 1)
    view = []
    recurse(root, 0)
    return view




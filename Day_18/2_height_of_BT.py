def maxDepthRecursive(root):
    return 1 + max(maxDepthRecursive(root.left), maxDepthRecursive(root.right)) if root else 0

# another solution is using BFS.
        
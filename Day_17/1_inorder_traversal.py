# Ref: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/283746/All-DFS-traversals-(preorder-inorder-postorder)-in-Python-in-1-line
# Q: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Left - Parent - Right

def recursiveInorder(root):
    # Time complexity: O(N). 
    # Space complexity: O(N) in worst case (linear tree; with no branches). Average case space: O(log N)
    return (recursiveInorder(root.left) + [root.val] + recursiveInorder(root.right)) if root else []

def iterativeInorder(root):
    # Time and space: O(N)
    stack = []
    traversal = []
    curr = root
    while curr!=None or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        traversal.append(curr.val)

        curr = curr.right
    
    return traversal

def iterativeInorderTwo(root):
    ans = []
    stack = []
    
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            ans.append(tmpNode.val)
            root = tmpNode.right
        
    return ans

def iterativeVisited(root):
    # This approach is nice as for preorder, inorder, postorder the code is almost the same. The only difference is the ordering of the append operations. While keeping in mind that stack is LIFO.
    
    stack = [(root, 'False')]
    traversal = []
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                traversal.append(node.val)
            elif node:
                stack.append((root.right, 'False'))
                stack.append((root, 'True'))
                stack.append((root.left, 'False'))
    return traversal

# Animation: https://docs.google.com/presentation/d/11GWAeUN0ckP7yjHrQkIB0WT9ZUhDBSa-WR0VsPU38fg/edit#slide=id.g61bfb572cf_0_125
# LC editorial: https://leetcode.com/problems/binary-tree-inorder-traversal/solution/

def MorrisTraversal(root):
    # O(N) time and O(1) space.
    traversal = []
    curr = root
    while curr:
        if curr.left:
            # Make current as right child of the rightmost node in current's left subtree
            predecessor = curr.left
            while predecessor.right and predecessor.right!=curr:
                predecessor = predecessor.right
            
            if not predecessor.right:
                predecessor.right = curr
                curr = curr.left
            else:
                # Revert back the changes in the tree
                predecessor.right = None
                traversal.append(curr.val)
                curr = curr.right

        else:
            traversal.append(curr.val)
            curr = curr.right
    return traversal

        
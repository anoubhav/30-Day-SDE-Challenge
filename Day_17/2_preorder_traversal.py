# Parent - Left - Right
# Q: https://leetcode.com/problems/binary-tree-preorder-traversal/

def recursivePreorder(root):
    # O(N) time and space.
    return ([root.val] + recursivePreorder(root.left) + recursivePreorder(root.right)) if root else []

def iterativePreorder(root):
    stack, traversal = [], []
    while stack or root:
        if root:
            traversal.append(root.val)
            stack.append(root)
            root = root.left
        else:
            tmpNode = stack.pop()
            root = tmpNode.right
    return traversal

def iterativePreorderTwo(root):
    # This solution can be obtained from the visited array function in inorder_traversal.py
    stack = [root]
    traversal = []
    while stack:
        node = stack.pop()
        if node:
            traversal.append(node.val)
            # stack is LIFO; we want left nodes to be processed first; hence we push it after right nodes
            stack.append(node.right)   
            stack.append(node.left)
    return traversal   

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
                traversal.append(curr.val)      ## In case of Preorder
                curr = curr.left
            else:
                # Revert back the changes in the tree
                predecessor.right = None
                # traversal.append(curr.val)   ## In case of Inorder
                curr = curr.right

        else:
            traversal.append(curr.val)
            curr = curr.right
    return traversal


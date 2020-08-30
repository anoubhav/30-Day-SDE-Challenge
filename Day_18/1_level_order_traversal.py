# Q: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

# time and space complexity: O(N)
def levelOrderBFS(root):
    from collections import deque # allows for O(1) popping from left ended. deque: double ended queue
    if not root: return []
    q = deque([(root, 0)])
    trav = []
    
    while q:
        node, level = q.popleft()
        if level >= len(trav):
            trav.append([])
        
        trav[level].append(node.val)
        
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return trav

def levelOrderBFS2(root):
    if not root: return []
    curr = [root]
    ans = []
    while curr:
        ans.append([node.val for node in curr])
        nxtlvl = []
        for node in curr:
            if node.left:
                nxtlvl.append(node.left)
            if node.right:
                nxtlvl.append(node.right)
        curr = nxtlvl
    return ans

# O(N) time and O(h) space. where n is the number of nodes, h is the height of the tree. h ~ log N in average case for balanced tree. h ~ N for unbalanced tree
def levelOrderDFS(root):

    # Perform a preorder traversal
    def dfs(node, level):
        if node:
            if level == len(trav):
                trav.append([])
            
            trav[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
    
    trav = []
    dfs(root, 0)
    return trav

            


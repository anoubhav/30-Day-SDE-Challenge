# Q: https://leetcode.com/problems/clone-graph/
# Ref: https://leetcode.com/problems/clone-graph/discuss/42314/Python-solutions-(BFS-DFS-iteratively-DFS-recursively)./420527


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# BFS - iterative
def cloneGraph(node):
    from collections import deque
    if not node: 
        return None
    
    q = deque([node])
    nodeCopy = Node(node.val)
    dic = {node: nodeCopy}
    
    while q:
        node = q.popleft()
        
        for nbr in node.neighbors:
            if nbr not in dic:
                tempNode = Node(nbr.val)
                dic[nbr] = tempNode
                dic[node].neighbors.append(dic[nbr])
                q.append(nbr)
                
            else:
                dic[node].neighbors.append(dic[nbr])

    return nodeCopy

# DFS - iterative
def cloneGraphDFS(node):
    from collections import deque
    if not node: 
        return None
    
    stack = [node]
    nodeCopy = Node(node.val)
    dic = {node: nodeCopy}
    
    while stack:
        node = stack.pop()
        
        for nbr in node.neighbors:
            if nbr not in dic:
                tempNode = Node(nbr.val)
                dic[nbr] = tempNode
                stack.append(nbr)
                dic[node].neighbors.append(dic[nbr])
                
            else:
                dic[node].neighbors.append(dic[nbr])

    return nodeCopy  
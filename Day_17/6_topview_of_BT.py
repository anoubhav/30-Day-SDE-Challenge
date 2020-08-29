# Q: https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1

def topView(root):
    from collections import deque, defaultdict
    
    q = deque([(root, 0)])
    l2r = defaultdict(int)
    
    while q:
        node, left = q.popleft()
        if l2r[left] == 0:
            l2r[left] = node.data # store the first node at a particular horizontal distance
        
        if node.left:
            q.append((node.left, left - 1))
            
        if node.right:
            q.append((node.right, left + 1))

    
    keys = sorted(l2r.keys())
    
    for k in keys:
        print(l2r[k], end = " ")
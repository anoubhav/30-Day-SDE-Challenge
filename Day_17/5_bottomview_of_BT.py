# Q: https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

def bottomView(root):
    from collections import deque, defaultdict
    
    q = deque([(root, 0)])
    l2r = defaultdict(int)
    
    while q:
        node, left = q.popleft()
        ## if l2r[left] == 0:

        l2r[left] = node.data  # always store the latest node at a horizontal particular distance.
        
        if node.left:
            q.append((node.left, left - 1))
            
        if node.right:
            q.append((node.right, left + 1))

    
    keys = sorted(l2r.keys())
    
    res = []
    for k in keys:
        res.append(l2r[k])
    return res
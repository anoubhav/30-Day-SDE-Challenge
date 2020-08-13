# Problem Link: https://www.geeksforgeeks.org/given-only-a-pointer-to-a-node-to-be-deleted-in-a-singly-linked-list-how-do-you-delete-it/
def delete(node):
    # Time complexity: O(1)
    
    # first node
    if node == head:
        temp = head.next
        del head
        head = temp
    else:
        nxt = node.next
        # last node
        if nxt == None:
            node.val = None
        else:
            # in between; copy the next node
            node.val = nxt.val
            node.next = nxt.next
            del nxt
            
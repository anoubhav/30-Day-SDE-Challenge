class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def createLL(self, arr):
        self.head = curr = ListNode(arr[0])
        n = len(arr)
        for i in range(n-1):
            nxt = ListNode(arr[i + 1])
            curr.next = nxt
            curr = curr.next

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.val, '->', end = " ")
            curr = curr.next
        print('None')
    
    def mergeLL(self, l2):
        # O(M + N) time complexity; O(N) space. Not in place. Returns a newly created linked list.
        prev = curr = ListNode(-1)
        h1, h2 = self.head, l2.head

        while h1 and h2:
            if h1.val <= h2.val:
                curr.next = h1
                h1 = h1.next
            else:
                curr.next = h2
                h2 = h2.next
            curr = curr.next
            
        if h1:
            curr.next = h1
        if h2:
            curr.next = h2
        
        return LinkedList(prev.next)

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.createLL([1, 2, 3 ,4, 7])
    ll1.printLL()

    ll2 = LinkedList()
    ll2.createLL([11, 13, 17])
    ll2.printLL()

    merged = ll1.mergeLL(ll2)
    merged.printLL()


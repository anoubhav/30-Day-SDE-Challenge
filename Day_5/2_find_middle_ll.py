class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

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
    
    def findMiddle(self):
        if not self.head: return self.head
        slow = fast = self.head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        print(slow.val)
        return slow

if __name__ == '__main__':
    ll = LinkedList()
    ll.createLL([1, 2, 3 ,4, 7])
    ll.printLL()
    ll.findMiddle()

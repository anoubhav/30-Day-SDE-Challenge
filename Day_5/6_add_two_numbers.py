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
    
    def addTwoLL(self, l2):
        # O(N) time and space. Returns a new linked list with the sum.
        newll = LinkedList()
        newll.createLL([1])
        dummy = newll.head

        curr = dummy
        l1 = self.head
        l2 = l2.head
        carry = 0

        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            s     = l1val + l2val + carry
            carry = 1 if s > 9 else 0
            s     = s - carry*10

            if l1: l1 = l1.next
            if l2: l2 = l2.next

            curr.val = s

            if l1 or l2:
                curr.next = ListNode(-1)
                curr = curr.next
        if carry:
            curr.next = ListNode(1)
        
        return newll

if __name__ == "__main__":
    l1 = LinkedList()
    l1.createLL([2, 0, 5, 9])
    l2 = LinkedList()
    l2.createLL([6, 9, 8, 2])

    l3 = l1.addTwoLL(l2)
    l3.printLL()

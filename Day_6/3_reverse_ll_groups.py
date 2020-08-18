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

    def reverseInGroups(self, k):
        def reverse(node, k):
            end = node
            prev = None
            while node and k:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
                k -= 1
            return prev, end
        
        slow = fast = self.head

        for _ in range(k):
            if fast.next:
                fast = fast.next
            else:
                return
        
        prev = ListNode(-1)
        prev.next = self.head

        curr = prev
        while True:
            start, end = reverse(slow, k)
            curr.next = start
            end.next = fast
            slow = fast

            try:
                for _ in range(k):
                    fast = fast.next
            except:
                self.head = prev.next
                return
        
            curr = end

        self.head = prev.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.createLL([1, 2, 3, 4, 5, 6, 7, 8, 9])
    ll.reverseInGroups(2)
    ll.printLL()

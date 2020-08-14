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

    def removeNthFromBackOnePass(self, n):
        dummy = ListNode(0)
        dummy.next = self.head
        first, second = dummy, dummy
        for _ in range(n):
            second = second.next

        if not second.next:
            # remove head node
            self.head = self.head.next

        else:
            while second.next:
                first = first.next
                second = second.next
            
            if first.next:
                first.next = first.next.next

    

    def removeNthFromBack(self, n):
        # Two pass solution. Time complexity: O(N). O(1) space.
        if not self.head: return
        # find the length l
        l = 1
        curr = self.head
        while curr.next:
            curr = curr.next
            l += 1
        
        toremove = l - n + 1
        
        # check if n is valid
        if toremove > 0:
            curr = self.head
            prev = None
            toremove -= 1
            while toremove:
                prev = curr
                curr = curr.next
                toremove -= 1

            if prev: 
                prev.next = curr.next
                del curr
            else:
                # remove head node
                nxt = self.head.next
                del self.head
                self.head = nxt

if __name__ == '__main__':
    ll1 = LinkedList()
    ll1.createLL([1, 2, 3 ,4, 7])
    ll1.printLL()
    ll1.removeNthFromBack(3)
    ll1.printLL()
    ll1.removeNthFromBackOnePass(4)
    ll1.printLL()
    

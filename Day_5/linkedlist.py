class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, val):
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = ListNode(val)
        else:
            self.head = ListNode(val)

    def prepend(self, val):
        if self.head:
            new = ListNode(val)
            new.next = self.head
            self.head = new
        else:
            self.val = ListNode(val)

    def extendLL(self, arr):
        n = len(arr)
        if not self.head:
            self.head = curr = ListNode(arr[0])
            for i in range(n-1):
                nxt = ListNode(arr[i + 1])
                curr.next = nxt
                curr = curr.next
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            
            for i in range(n):
                nxt = ListNode(arr[i])
                curr.next = nxt
                curr = curr.next

    def deleteNode(self, val):
        if self.head:
            if self.head.val == val:
                self.head = self.head.next
            else:
                curr = self.head
                found = False
                while curr.next:
                    if curr.next.val == val:
                        found = True
                        break
                    curr = curr.next
                if found:
                    curr.next = curr.next.next

    def printLL(self):
        curr = self.head
        while curr:
            print(curr.val, '->', end = " ")
            curr = curr.next
        print('None')

if __name__ == '__main__':
    ll = LinkedList()
    ll.append(101)
    ll.extendLL([1, 2, 3, 4])
    ll.printLL()
    ll.extendLL([9, 8, 11])
    ll.printLL()
    ll.prepend(999)
    ll.append(4)
    ll.printLL()
    ll.deleteNode(101)
    ll.deleteNode(4)
    ll.deleteNode(4)
    ll.deleteNode(4)
    ll.deleteNode(999)
    ll.printLL()




        
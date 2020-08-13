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
    
    def reverseLL(self):
        prev = None
        curr = self.head

        while curr:
            curr.next, prev, curr = prev, curr, curr.next

            ## OR
            # nxt = curr.next
            # curr.next = prev
            # prev = curr
            # curr = nxt
        self.head = prev
    
    def reverseLL_recursive(self):
        if not self.head: return self.head
        def recurse(prev, curr):
            if curr == None:
                self.head.next = None
                self.head = prev
                return            
            recurse(curr, curr.next)
            curr.next = prev

        recurse(None, self.head)

        ## Also see solution without using prev node.Ref: https://www.youtube.com/watch?v=MRe3UsRadKw

        # if not self.head: return self.head
        # def recurse2(curr):
        #     if curr.next == None:
        #         return curr      
        #     self.head = recurse(curr.next)
        #     curr.next.next = curr
        #     curr.next = None
            
        #     return self.head
        # return recurse(self.head)

if __name__ == '__main__':
    ll = LinkedList()
    ll.createLL([1, 2, 3 ,4, 7])
    ll.printLL()
    ll.reverseLL()
    ll.printLL()
    ll.reverseLL_recursive()
    ll.printLL()
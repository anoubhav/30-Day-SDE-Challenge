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
    
    # Ref: https://www.youtube.com/watch?v=vHam6riSavo
    def isPalindrome(self):
        # Time complexity : O(N). Space: O(1). Modifies the array. You can reverse the array a second time and combine to undo the changes.

        # find the middle of the linked list. In O(N)
        fast = slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # move the fast pointer to the beginning of the linked list.
        fast = self.head


        # reverse the second half of the linked list in O(1)
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Compare the first half and the second half of the linked list
        while prev:
            if fast.val != prev.val:
                return False
            prev = prev.next
            fast = fast.next
        return True

    def isPalindromeExtraSpace(self):
        # Time and space complexity : O(N)
        vals = []
        curr = self.head
        while curr:
            vals += curr.val,
            curr = curr.next
        print(vals)
        return vals == vals[::-1]
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.createLL([1, 2, 3, 4, 3, 2, 1])
    print(ll.isPalindromeExtraSpace())
    print(ll.isPalindrome())

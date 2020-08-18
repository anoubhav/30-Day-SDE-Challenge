def naive(headA, headB):
    # Time complexity: O(MN). Space O(1)
    while headA:
        curr = headB
        while curr:
            if headA == curr:
                return curr
            curr = curr.next
        headA = headA.next
    return None

def usingMap(headA, headB):
    # Time complexity: O(N). Space O(N)

    if not headA or not headB: return None
    
    seen = set()
    while headA:
        seen.add(headA)
        headA = headA.next
    
    while headB:
        if headB in seen:
            return headB
        headB = headB.next
    return None

def twoPointer(headA, headB):
    # O(M + N) time complexity; where M, N are sizes of the linked lists. O(1) space.
    if not headA or not headB: return None

    p1, p2 = headA, headB
    while p1!=p2:
        p1, p2 = p1.next, p2.next
        if p1 == p2 or (not p1 and not p2): break
        if not p1: p1 = headB
        if not p2: p2 = headA
    return p1

def changeNegative(headA, headB):
    # The problem description says that all values are positive, no circular links in either list, and no '0' values at the intersection node. You replace all the values in List A with their negatives, and you traverse List B until you find a negative value. Only remaining task is to undo the changes before returning the answer.

    # O(M + N) time complexity; O(1) space.
    curr = headA
    while curr:
        curr.val *= -1
        curr = curr.next
    
    curr = headB
    ans = None
    while curr:
        if curr.val < 0:
            ans = curr
            break
        curr = curr.next
    
    curr = headA
    while curr:
        curr.val *= -1
        curr = curr.next

    return ans
            




## Intuition for two pointer approach:
# Instead of thinking about it as switching from the end of list A to the beginning of list B I think about it as iterating through a single list C whose contents are list A, then list B in order and a single list D whose contents are list B, then list A in order. Now we have two lists of equal length which we are iterating through rather than two linked lists of differing sizes. Since we know that these two lists do intersect, we know that both C and D will end with the same X elements  (where X is the number of overlapping elements from A and B) and that the first of these elements will be from the  node at which they intersect. So thinking of it this way, the code is essentially iterating through C and D simultaneously and checking if their current nodes match. Since both C and D are the same length and end in the same elements, it is guaranteed that if they intersect this code will return the correct node.
def floyd_tortoise_hare(head):
    # O(N) time complexity, O(1) space.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: break
    else: return None

    while head!=slow:
        head = head.next
        slow = slow.next
    return slow

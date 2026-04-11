# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Mid node using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half (Slowing pointing to mid node)
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_curr = curr.next
            curr.next = prev 
            prev = curr
            curr = next_curr

        # Merge two lists (everyother element), prev pointing to head of revesed list
        # head -> first half
        # prev -> reversed second half
        while head and prev:
            next_head = head.next
            next_prev = prev.next
            head.next = prev
            prev.next = next_head
            head = next_head
            prev = next_prev
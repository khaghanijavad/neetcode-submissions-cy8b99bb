# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev_tail = dummy
        
        while head:
            # Step 1: check if we have k nodes
            node = head
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            
            if count < k:
                break  # not enough nodes, leave as-is
            
            # Step 2: cut the segment
            kth = head
            for _ in range(k - 1):
                kth = kth.next
            
            next_group = kth.next
            kth.next = None  # isolate segment
            
            # Step 3: reverse
            rev_head = self.reverseList(head)
            
            # Step 4: reconnect
            prev_tail.next = rev_head
            head.next = next_group  # head is now tail after reverse
            
            # Step 5: move pointers
            prev_tail = head
            head = next_group
        
        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        return prev
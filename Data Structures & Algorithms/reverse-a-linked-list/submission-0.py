# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        new_node = head
        if head.next:
            new_node = self.reverseList(head.next)
            head.next.next = head

        head.next = None
        
        return new_node

# val = 0, next_node = [1]
    # val = 1, next_node = [2]
        # val = 2, next_node = [3]
            # val= 3, next_node = None

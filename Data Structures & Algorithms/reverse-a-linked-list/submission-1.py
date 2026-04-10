# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev 
            prev = curr
            curr = temp
        return prev
            
        

# val = 0, next_node = [1]
    # val = 1, next_node = [2]
        # val = 2, next_node = [3]
            # val= 3, next_node = None

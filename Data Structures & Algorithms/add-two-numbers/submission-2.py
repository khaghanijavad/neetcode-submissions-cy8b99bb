# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = l1, l2

        c = 0
        curr_out = sum_node = ListNode(c)
        while curr1 or curr2:
            val1 = curr1.val if curr1 else 0
            val2 = curr2.val if curr2 else 0 
            s = val1 + val2 + curr_out.val
            curr_out.val = s % 10 
           
            c = s // 10
            temp = ListNode(c)

            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None

            if curr1 or curr2 or c:
                curr_out.next = temp
            
            curr_out = curr_out.next
    
        return sum_node
        
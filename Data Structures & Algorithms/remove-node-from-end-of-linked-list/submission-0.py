# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = rev_list = self.rev(head)

        # n=1 after reversal means remove the new head
        if n == 1:
            new_head = rev_list.next
            return self.rev(new_head)
        counter =  1  
        while curr:
            if counter == n-1:
                curr.next = curr.next.next
                break
            curr = curr.next
            counter += 1
        return self.rev(rev_list)


    
    def rev(self, head):
        prev, curr = None, head
        while curr: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

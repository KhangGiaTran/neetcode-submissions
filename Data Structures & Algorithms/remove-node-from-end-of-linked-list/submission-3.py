# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        removeIndex = length - n
        if removeIndex == 0:
            return head.next

        # walk until node before target
        curr = head
        for i in range(removeIndex - 1):
            curr = curr.next

        curr.next = curr.next.next
        
        return head
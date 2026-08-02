# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        compare1, compare2 = list1, list2
        head = ListNode()
        dummy = head

        while compare1 and compare2:
            if compare1.val < compare2.val:
                head.next = compare1
                compare1 = compare1.next
            else:
                head.next = compare2
                compare2 = compare2.next
            head = head.next
        
        if compare1:
            head.next = compare1
        else:
            head.next = compare2

        return dummy.next
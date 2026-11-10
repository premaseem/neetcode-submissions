# Q https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        1. start new list, look at both list element value and pick the smaller one from both 
        """

        if not list1: 
            return list2
        if not list2:
            return list1 
        
        if list1.val <= list2.val: 
            newlist = list1
            list1 = list1.next
        else:
            newlist = list2 
            list2 = list2.next 

        newHead = newlist
        while list1 or list2: 
            e1 = e2 = 0
            if list1:
                e1 = list1.val
            if list2:
                e2 = list2.val 
            if list1 and (not list2 or e1 <= e2 ):
                newlist.next = list1
                list1 = list1.next
            elif list2:
                newlist.next = list2
                list2 = list2.next 
            if newlist:
                newlist = newlist.next

        return newHead 
            

        
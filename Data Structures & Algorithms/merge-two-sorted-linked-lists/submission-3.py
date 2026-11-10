# Q https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        start new list, iterate and link back the remaining list  
        """
        if not list1:
            return list2
        if not list2:
            return list1 

        if list1.val <= list2.val: 
            newHead = list1 
            list1 = list1.next 
        else :
            newHead = list2 
            list2 = list2.next 
        
        list3 = newHead
        while list1 and list2:
            if list1.val <= list2.val: 
                list3.next = list1
                list1 = list1.next 
            else: 
                list3.next = list2
                list2 = list2.next 
            list3 = list3.next 
        list3.next = list1 or list2 
        return newHead 


            

        
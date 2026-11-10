# Q https://neetcode.io/problems/merge-two-sorted-linked-lists/question?list=neetcode150 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        convert in array of nodes and sort by val
        iterate new array and link nodes.   
        """
        if not list1:
            return list2 
        if not list2:
            return list1 

        list3 = []
        while list1:
            list3.append(list1)
            list1 = list1.next 

        while list2: 
            list3.append(list2)
            list2 = list2.next 

        list3.sort(key=lambda o:o.val)

        for i in range(1,len(list3)):
            list3[i-1].next = list3[i]
        

        list3[-1].next = None 
        
        return list3[0]







            

        
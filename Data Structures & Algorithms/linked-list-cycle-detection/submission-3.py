# Q https://neetcode.io/problems/linked-list-cycle-detection/question
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 2. slow and fast point 
        """
        iternate slow by 1 and fast pointer by 2 
        if fast pointer reaches null as next node, it is not cycle 
        keep checking if value of both fast and slow pointer is same that means, they are cycling and colided now return True 
        """
        if not head:
            return False
        sp = head 
        fp = sp.next
        while sp and fp: 
            if sp.val == fp.val:
                return True 
            sp = sp.next 
            if fp.next:
                fp = fp.next.next
            else: 
                fp = fp.next
             
        return False
        
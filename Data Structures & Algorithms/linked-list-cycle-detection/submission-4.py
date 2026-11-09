# Q https://neetcode.io/problems/linked-list-cycle-detection/question
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 2. slow and fast pointer with Try except
        """
        iternate slow by 1 and fast pointer by 2 
        if any pointer reaches null and throw AttributeError of NPE, it it is not cyclic 
        """
        slow = fast = head 
        try: 
            while True: 
                slow = slow.next 
                fast = fast.next.next 
                if slow is fast:
                    return True 

        except: 
            return False 
        
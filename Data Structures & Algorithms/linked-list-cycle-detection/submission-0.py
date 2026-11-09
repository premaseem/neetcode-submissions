# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 1. iterate and put in seen kv map 
        n = head
        idx = 0
        seen = {}
        while n:
            nodevalue= seen.get(n.val, None)
            if not nodevalue: 
                seen[n.val] = idx
            else:
                return True
            idx += 1 
            n = n.next         
        return False
        
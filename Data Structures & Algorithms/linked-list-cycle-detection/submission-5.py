# Q https://neetcode.io/problems/linked-list-cycle-detection/question
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 3. seen using the set
        """
        through node in set and check
        """
        node = head
        seen = set()
        while node: 
            if node in seen:
                return True 
            else: 
                seen.add(node)
            node = node.next 
            
        return False 

        
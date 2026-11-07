# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative O(n) solutoin 
        if not head:
            return head

        node = head
        nodelist = []
        while node :
            nodelist.append(node)
            node = node.next
        
        rlist = nodelist[::-1] 
        head = rlist[0]
        last = rlist[-1]
        last.next = None
        for i in range(len(rlist)-1):
            rlist[i].next = rlist[i+1]

        node = head
        while node:
            print(node.val)
            node = node.next 
        return head 


        
        
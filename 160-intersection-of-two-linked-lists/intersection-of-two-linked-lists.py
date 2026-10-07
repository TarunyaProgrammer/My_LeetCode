# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # A,B = headA,headB
        # while A!=B:
        #     if A == None:
        #         A=headB
        #     else:
        #         A = A.next
        #     if B == None:
        #         B=headA
        #     else:
        #         B = B.next
        # return A
        
        res={}
        slow=headA
        while slow:
            res[slow]=1
            slow=slow.next
        fast=headB
        while fast:
            if fast in res:
                return fast
            fast=fast.next
        return None
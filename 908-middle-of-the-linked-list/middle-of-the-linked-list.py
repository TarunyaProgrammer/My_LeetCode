# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 0
        # temp1 = head
        # while temp1:
        #     length +=1
        #     temp1 = temp1.next
        # temp2 = head
        # for i in range(length//2):
        #     temp2 = temp2.next
        # return temp2

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)

        front = dummy
        back = dummy
        for _ in range(n):
            back = back.next

        while True:
            if not back.next:
                front.next = front.next.next
                break
            else:
                front = front.next
                back = back.next


        return dummy.next
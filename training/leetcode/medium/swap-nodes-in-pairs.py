# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        save = head
        if head is None:
            return head
        while head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next
            if head.next and head.next.next:
                head = head.next
            else:
                break
        return save
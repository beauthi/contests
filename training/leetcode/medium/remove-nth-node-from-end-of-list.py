# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        ptr = head
        while n:
            ptr = ptr.next
            n -= 1
        save = head
        previous = None
        while ptr:
            previous = head
            head = head.next
            ptr = ptr.next
        if previous is None:
            save = save.next
        else:
            previous.next = head.next
        return save
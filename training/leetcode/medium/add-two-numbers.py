# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        cur = None
        prev = None
        save = None
        r = 0
        while l1 or l2:
            if not l2:
                cur = ListNode((l1.val + r) % 10)
                prev.next = cur
                prev = cur
                r = int((l1.val + r) / 10)
                l1 = l1.next
            elif not l1:
                cur = ListNode((l2.val + r) % 10)
                prev.next = cur
                prev = cur
                r = int((l2.val + r) / 10)
                l2 = l2.next
            else:
                cur = ListNode((l1.val + l2.val + r) % 10)
                if prev:
                    prev.next = cur
                else:
                    save = cur
                r = int((l1.val + l2.val + r) / 10)
                prev = cur
                l1 = l1.next
                l2 = l2.next
        prev.next = None if not r else ListNode(r)
        return save
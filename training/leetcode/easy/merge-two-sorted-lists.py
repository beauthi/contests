# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 == None and l2 == None:
            return None
        l = list()
        while l1:
            l.append(l1.val)
            l1 = l1.next
        while l2:
            l.append(l2.val)
            l2 = l2.next
        l.sort()
        res = ListNode(l[0])
        ptr = res
        for i in range(1, len(l)):
            res.next = ListNode(l[i])
            res = res.next
        return ptr
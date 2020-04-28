# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: list) -> ListNode:
        res = None
        ptr = None
        lists = sorted([l for l in lists if l is not None], key=lambda x: x.val)
        while len(lists) > 0:
            if res is None:
                res = ListNode(lists[0].val)
                ptr = res
            else:
                ptr.next = ListNode(lists[0].val)
                ptr = ptr.next
            lists[0] = lists[0].next
            lists = sorted([l for l in lists if l is not None], key=lambda x: x.val)
        return res

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
l = [l1, l2, l3]
elt = s.mergeKLists(l)
while elt is not None:
    print(elt.val)
    elt = elt.next
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printList(self, l1):
        elt = l1
        while elt is not None:
            print(elt.val, end=" ")
            elt = elt.next
        print()
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None:
            return None
        if k == 1 or head.next == None:
            return head
        new_tail = head
        prev = head
        new = prev.next
        prev_tail = None
        if new is not None:
            nxt = new.next
        first = True
        count_left_nodes = 1
        counter = new
        while counter is not None:
            counter = counter.next
            count_left_nodes += 1
        while new is not None and count_left_nodes >= k:
            n = 0
            while n < (k - 1) and new is not None:
                new.next = prev
                prev = new
                new = nxt
                if new is not None:
                    nxt = new.next
                n += 1
            if first:
                head = prev
                first = False
            else:
                new_head = prev
                prev_tail.next = new_head
            prev_tail = new_tail
            new_tail.next = new
            new_tail = new

            prev = new
            if prev is not None:
                new = prev.next
            if new is not None:
                nxt = new.next
            count_left_nodes = 1
            counter = new
            while counter is not None:
                counter = counter.next
                count_left_nodes += 1
        return head

s = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(7)
l1.next.next.next.next.next.next.next = ListNode(8)
print("n = 2")
s.printList(l1)
elt = s.reverseKGroup(l1, 2)
s.printList(elt)
print("n = 3")
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
l1.next.next.next.next.next.next = ListNode(7)
l1.next.next.next.next.next.next.next = ListNode(8)
s.printList(l1)
elt = s.reverseKGroup(l1, 3)
s.printList(elt)

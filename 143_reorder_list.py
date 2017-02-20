# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow = head
        fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        p1 = head
        prev.next = None
        p2 = slow
        # reverse p2
        p2_prev = None
        cur = p2
        while cur is not None:
            p2_next = cur.next
            cur.next = p2_prev
            p2_prev = cur
            cur = p2_next
        p2 = p2_prev
        # merge p1 and p2
        p1_cur = p1
        p2_cur = p2
        p1_next = p1_cur.next
        p2_next = p2_cur.next
        while p1_cur:
            p1_next = p1_cur.next
            p2_next = p2_cur.next
            p1_cur.next = p2_cur
            if p1_next:
                p1_cur.next.next = p1_next
                p1_cur = p1_next
                p2_cur = p2_next
            else:
                break

    @staticmethod
    def createList(arr):
        head = None
        p = None
        for i in arr:
            node = ListNode(i)
            if head is None:
                head = node
                p = node
            else:
                p.next = node
                p = p.next
        return head

    @staticmethod
    def printList(p):
        while p is not None:
            print p.val
            p = p.next

def testcase(test_data):
    p = Solution.createList(test_data)
    result = Solution().reorderList(p)
    Solution.printList(result)
    print 'end\n'

if __name__ == '__main__':
    testcase([1, 2, 3, 4, 5, 6])
    testcase([1, 2, 3, 4, 5, 6, 7])

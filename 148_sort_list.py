# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        prev = None
        if head is None or head.next is None:
            return head
        while p1 and p2 and p2.next:
            prev = p1
            p1 = p1.next
            p2 = p2.next.next
        if prev:
            prev.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(p1)
        return self.merge(l1, l2)

    def merge(self, p1, p2):
        #print 'merge ', Solution.printList(p1), Solution.printList(p2)
        head = ListNode(None)
        p = head
        while p1 or p2:
            if p1 is None:
                p.next = p2
                p2 = p2.next
            elif p2 is None:
                p.next = p1
                p1 = p1.next
            else:
                if p1.val <= p2.val:
                    p.next = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p2 = p2.next
            p = p.next
        return head.next

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
        result = ''
        while p is not None:
            result = result + str(p.val) + ' '
            p = p.next
        print 'print list: ', result

if __name__ == '__main__':
    p1 = Solution.createList([1, 3, 2, 4, 7, 9, 6, 8])
    Solution.printList(p1)
    result = Solution().sortList(p1)
    Solution.printList(result)

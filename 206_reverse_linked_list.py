# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

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

if __name__ == '__main__':
    p1 = Solution.createList([1, 2, 3, 4])
    #Solution.printList(p1)
    p2 = Solution().reverseList(p1)
    Solution.printList(p2)

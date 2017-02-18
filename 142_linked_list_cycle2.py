# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p1 = head
        p2 = head
        while True:
            if p1 == None or p2 == None:
                return None
            p1 = p1.next
            p2 = p2.next
            if p2 == None:
                return None
            p2 = p2.next
            if p1 == p2:
                break
        p1 = head
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1        

    @staticmethod
    def createList(arr):
        head = None
        p = None
        for i in arr:
            node = ListNode(i)
            if head == None:
                head = node
                p = node
            else:
                p.next = node
                p = p.next
        p.next = head.next
        return head

if __name__ == '__main__':
    p1 = Solution.createList([1,2,3,4])
    node = Solution().detectCycle(p1)
    if node:
        print node.val
    else:
        print 'None'

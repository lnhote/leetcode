# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from Queue import PriorityQueue
        q = PriorityQueue()
        dummy = ListNode(None)
        cur = dummy
        for l in lists:
            if l:
                q.put((l.val, l))
        while q.qsize() > 0:
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return dummy.next


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
        return head

    @staticmethod
    def printList(p):
        while p != None:
            print p.val
            p = p.next

if __name__ == '__main__':
    p1 = Solution.createList([1,3,5,7])
    p2 = Solution.createList([2,4,6,8])
    p = Solution().mergeKLists([p1, p2])
    Solution.printList(p)

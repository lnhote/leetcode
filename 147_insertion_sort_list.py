# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        result = head
        head = head.next
        result.next = None
        while head:
            # compare head with values in result list
            result_ptr = result
            prev = None
            next_one = head.next
            #print '\nadd %d to result' % (head.val), Solution.listStr(result)
            while result_ptr:
                #print 'check result value: ', result_ptr.val
                if head.val >= result_ptr.val:
                    prev = result_ptr
                    result_ptr = result_ptr.next
                else:
                    if prev:
                        prev.next = head
                        prev.next.next = result_ptr
                    else:
                        result = head
                        result.next = result_ptr
                    break
            if result_ptr is None and head.val >= prev.val:
                #print head.val, 'larger than all', prev.val
                head.next = None
                prev.next = head
            head = next_one
        return result

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
        print 'print list: ', Solution.listStr(p)

    @staticmethod
    def listStr(p):
        result = ''
        while p is not None:
            result = result + str(p.val) + ' '
            p = p.next
        return result

if __name__ == '__main__':
    p1 = Solution.createList([1, 3, 2, 4, 7, 9, 6, 8])
    Solution.printList(p1)
    result = Solution().insertionSortList(p1)
    Solution.printList(result)

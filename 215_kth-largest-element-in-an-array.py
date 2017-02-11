class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        length = len(nums)
        end = length - 1

        while start < end:
            mid = self.partition(nums, start, end)
            # print nums, 'mid = %d, start[%d] = [%d], end[%d] = %d' % (mid, start, nums[start], end, nums[end])
            if k < length - mid:
                if mid == start:
                    start = mid + 1
                else:
                    start = mid
            elif k > length - mid:
                end = mid - 1
            else:
                break
        # print 'end:', nums, start, end
        return nums[length-k]

    def partition(self, nums, start, end):
        pivot = nums[start]
        old_start = start
        old_end = end
        length = len(nums)
        while start < end:
            while start < end and nums[end] >= pivot:
                end = end - 1

            nums[start] = nums[end]
            while start < end and nums[start] <= pivot:
                start = start + 1
            nums[end] = nums[start]
            nums[start] = pivot
        return start


if __name__ == '__main__':
    print Solution().findKthLargest([3,2,1,5,6,4],2) #2th = 5
    print Solution().findKthLargest([1],1) #1th = 1
    print Solution().findKthLargest([3,2,3,1,2,4,5,5,6],9) #9th = 1
    print Solution().findKthLargest([5,2,4,1,3,6,0], 4) #4th = 3
    print Solution().findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 2) #2th = 10
    print Solution().findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6], 20) #20th = 2

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.partition(nums, 0, len(nums)-1, k)


    def partition(self, nums, start, end, k):
        print 'start ', start, end, nums
        pivot = nums[start]
        old_start = start
        old_end = end
        length = len(nums)
        while start < end and nums[end] >= pivot:
            end = end - 1

        nums[start] = nums[end]
        while start < end and nums[start] <= pivot:
            start = start + 1
        nums[end] = nums[start]
        nums[start] = pivot
        print 'end ', start, end, nums
        if k < length - end:
            return self.partition(nums, end+1, old_end, k)
        elif k == length - end:
            return nums[end]
        else:
            return self.partition(nums, old_start, end, k)


if __name__ == '__main__':
    # print Solution().findKthLargest([3,2,1,5,6,4],2) #2th = 5
    # print Solution().findKthLargest([1],1) #1th = 1
    # print Solution().findKthLargest([3,2,3,1,2,4,5,5,6],9) #9th = 1
    print Solution().findKthLargest([5,2,4,1,3,6,0], 4) #4th = 3

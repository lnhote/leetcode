class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_result = 0;
        result = 0;
        for i in range(len(nums)):
            if nums[i] == 1:
                result = result + 1
                if result > max_result:
                    max_result = result
            else:
                result = 0
        return max_result

if __name__ == '__main__':
    print Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])
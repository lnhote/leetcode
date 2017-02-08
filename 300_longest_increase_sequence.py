class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        matrix = [1]*length
        max_num = 1
        for i in range(length-1, -1, -1):
            for j in range(i, length):
                if nums[j] > nums[i]:
                    matrix[i] = max(matrix[i], 1+matrix[j])
                    if matrix[i] > max_num:
                        max_num = matrix[i]
        # print matrix
        return max_num

if __name__ == '__main__':
    print Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) # [2, 3, 7, 101], 4
    print Solution().lengthOfLIS([10,9,100]) # 1
    print Solution().lengthOfLIS([10]) # 1
    print Solution().lengthOfLIS([]) # 0

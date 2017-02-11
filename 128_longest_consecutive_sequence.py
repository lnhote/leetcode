class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_map = {}
        max_len = 1
        if len(nums) == 0:
            return 0
        for i, num in enumerate(nums):
            if num not in num_map:
                num_map[num] = 1
                
                length = 1
                left = right = num
                
                if num-1 in num_map:
                    length = length + num_map[num-1]
                    left = num - num_map[num-1]
                if num+1 in num_map:
                    length = length + num_map[num+1]
                    right = num + num_map[num+1]
                num_map[left] = length
                num_map[right] = length
                if length > max_len:
                    max_len = length
            else:
                pass
        return max_len
                

if __name__ == '__main__':
	print Solution().longestConsecutive([100, 4, 200, 1, 3, 2,5]) # 5

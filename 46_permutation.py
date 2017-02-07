class Solution(object):
    """docstring for Solution"""
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permuteResult([], nums)

    def permuteResult(self, result, nums):
        import copy
        new_result = []
        
        if len(nums) == 1:
            perm_item = copy.deepcopy(result)
            perm_item.append(nums[0])
            new_result.append(perm_item)
        else:
            for j in range(0, len(nums)):
                perm_item = copy.deepcopy(result)
                perm_item.append(nums[j])
                subresult = []
                if j == 0:
                    subresult = self.permuteResult(perm_item, nums[1:])
                elif j == len(nums) -1:
                    subresult = self.permuteResult(perm_item, nums[0:-1])
                else:
                    subresult = self.permuteResult(perm_item, nums[0:j]+nums[j+1:])
                for k in range(0, len(subresult)):
                    new_result.append(copy.deepcopy(subresult[k]))
        return new_result
        
if __name__ == '__main__':
    print Solution().permute([1,2,3])
    print Solution().permute([1,2,3,4])
        
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        T = [0]*length
        parent = [0]*length
        nums.sort()
        max_index = 0
        max_len = 0
        for i in range(length-1,-1,-1):
            item1 = nums[i]
            for j in range(i, length):
                item2 = nums[j]
                if item2%item1 == 0 and T[i] < T[j] + 1:
                    T[i] = T[j] + 1
                    parent[i] = j
                    if T[i] > max_len:
                        max_len = T[i]
                        max_index = i
        
        result = []
        for i in range(0, max_len):
            result.append(nums[max_index])
            max_index = parent[max_index]
        return result

if __name__ == '__main__':
    print Solution().largestDivisibleSubset([1,2,4,8,3,7,5]) #[1,2,4,8]
    print Solution().largestDivisibleSubset([3,5]) #[3]
    print Solution().largestDivisibleSubset([546,649]) #[546]
    print Solution().largestDivisibleSubset([]) #[]
    print Solution().largestDivisibleSubset([1]) #[1]
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        str1 = strs[0]
        for i in range(0, len(str1)):
            letter = str1[i]
            for j in range(1, len(strs)):
                str2 = strs[j]
                if len(str2) <= i or str2[i] != letter:
                    return prefix

            prefix = prefix + letter
        return prefix

if __name__ == '__main__':
    # print Solution().longestCommonPrefix(['aab', 'abc'])
    print Solution().longestCommonPrefix(['a', 'a', 'b'])
    # print Solution().longestCommonPrefix(['aab', 'aabc'])
    # print Solution().longestCommonPrefix(['aabd', 'aabc'])
    # print Solution().longestCommonPrefix(['', 'aabc'])
    # print Solution().longestCommonPrefix(['', ''])
    # print Solution().longestCommonPrefix([''])
    # print Solution().longestCommonPrefix([])

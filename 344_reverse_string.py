class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for i in range(len(s)-1,-1,-1):
            result.append(s[i])
        return ''.join(result)

    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        result.reverse()
        return ''.join(result)

if __name__ == '__main__':
    print Solution().reverseString('hello')
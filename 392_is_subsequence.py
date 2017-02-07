class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        slen = len(s)
        tlen = len(t)
        if tlen == 0:
            if slen != 0:
                return False
        if slen == 0:
            return True
        si = 0
        for i in range(0, tlen):
            if t[i] == s[si]:
                si = si + 1
                if si == slen:
                    return True
        return False

if __name__ == '__main__':
    print Solution().isSubsequence('abc', 'ahbgdc') #True
    print Solution().isSubsequence('axc', 'ahbgdc') #False
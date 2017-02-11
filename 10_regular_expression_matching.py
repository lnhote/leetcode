class Solution(object):
    def isMatch1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #print 'matching %s %s' % (s, p)
        if p == '':
            return len(s)==0
        if len(p) > 1 and p[1] == '*':
            if self.isMatch1(s, p[2:]):
                return True
            else:
                if len(s) == 0:
                    return False
                if s[0] != p[0] and p[0] != '.':
                    return False
                return self.isMatch1(s[1:], p)
        else:
            if len(s) == 0:
                return False
            if s[0] != p[0] and p[0] != '.':
                return False
            return self.isMatch1(s[1:], p[1:])
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False for j in range(0,(len(p)+1))] for i in range(0, (len(s)+1))]
        dp[0][0] = True
        for i in range(1, len(s)+1):
            dp[i][0] = False
        for i in range(1, len(p)+1):
            dp[0][i] = i>1 and dp[0][i-2] and p[i-1] == '*'
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    if j < 2:
                        return False
                    if dp[i][j-2]:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')
                else:
                    if i-1 >= len(s):
                        dp[i][j] = False
                    else:
                        dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        
        return dp[len(s)][len(p)]

if __name__ == '__main__':
    
    print Solution().isMatch("aa", "a") #false
    print Solution().isMatch("aa", "aa") #true
    print Solution().isMatch("aaa", "aa") # false
    print Solution().isMatch("aa", "a*") # true
    print Solution().isMatch("aa", ".*") # true
    print Solution().isMatch("ab", ".*") # true
    print Solution().isMatch("aab", "c*a*b") # true
    print Solution().isMatch("ab", ".*c") # false
    print Solution().isMatch("aaa", "a*a") # true
    
    print Solution().isMatch("", ".*") # true


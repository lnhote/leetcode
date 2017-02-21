class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(0, len(s))]
        for i in range(0, len(s)):
            for word in wordDict:
                if len(word)-1 > i:
                    continue
                if s[i-len(word)+1:i+1] != word:
                    if dp[i] is not True:
                        dp[i] = False
                else:
                    #print i, s[i-len(word)+1:i+1], word
                    if i-len(word) < 0:
                        dp[i] = True
                    else:
                        if dp[i] is not True:
                            dp[i] = dp[i-len(word)]
                        else:
                            dp[i] = True
                    #print dp
        return dp[len(s)-1]

if __name__ == '__main__':
    print Solution().wordBreak('leetcode', ['leet', 'code'])
    print Solution().wordBreak('abcd', ["a","abc","b","cd"])

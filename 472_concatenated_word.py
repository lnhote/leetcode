class TrieNode(object):
    def __init__(self, c):
        self.c = c
        self.children = {}
        self.isWord = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode('')

    def dfs(self, s):
        root = self.root
        for ch in s:
            if ch in root.children:
                root = root.children[ch]
            else:
                return False
        return root.isWord

    def insert(self, s):
        root = self.root
        for ch in s:
            if ch in root.children:
                root = root.children[ch]
            else:
                root.children[ch] = TrieNode(ch)
                root = root.children[ch]
        root.isWord = True


class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(0, len(s))]
        word_set = set(wordDict)
        for i in range(0, len(s)):
            for j in range(0, i+1):
                if j == 0 and s[j:i+1] in word_set:
                    if i != len(s)-1:
                        dp[i] = True
                        break
                elif j > 0 and dp[j-1] is True and s[j:i+1] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)-1]

    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        wordDict = set(words)
        for i, word in enumerate(words):
            word_len = len(word)
            if word_len is 0:
                continue
            dp = [False for i in range(0, word_len)]
            for i in range(0, word_len):
                for j in range(0, i+1):
                    if j == 0 and word[j:i+1] in wordDict:
                        if i != word_len-1:
                            dp[i] = True
                            break
                    elif j > 0 and dp[j-1] is True and word[j:i+1] in wordDict:
                        dp[i] = True
                        break
            if word_len > 0 and dp[word_len-1]:
                result.append(word)
            wordDict.add(word)
        return result

if __name__ == '__main__':
    print Solution().wordBreak('leetcode', ['leet', 'code'])
    print Solution().findAllConcatenatedWordsInADict(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"])
    print Solution().findAllConcatenatedWordsInADict(["cat"])
    print Solution().findAllConcatenatedWordsInADict([""])

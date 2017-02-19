class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        base_ascii = ord('a')
        bucket = [-1 for i in range(0, 26)]
        for pos, ch in enumerate(s):
            bucket[ord(ch)-base_ascii] = pos
        start = 0
        result = ''
        while True:
            min_pos = len(s)
            min_pos_ch = ''
            # find the letter with smallest index
            for i in range(0, 26):
                if bucket[i] > -1 and bucket[i] < min_pos:
                    min_pos = bucket[i]
                    min_pos_ch = chr(i+base_ascii)
            if min_pos == len(s):
                break
            end = min_pos
            # find the smallest letter before that index
            for i in range(end, start-1, -1):
                if s[i] <= min_pos_ch and bucket[ord(s[i])-base_ascii] > -1:
                    min_pos_ch = s[i]
                    min_pos = i
            bucket[ord(min_pos_ch)-base_ascii] = -1
            result = result + min_pos_ch
            start = min_pos + 1
        return result

if __name__ == '__main__':
    print Solution().removeDuplicateLetters('bcabc') # abc
    print Solution().removeDuplicateLetters('cbacdcbc') # acdb
    print Solution().removeDuplicateLetters('c') # c
    print Solution().removeDuplicateLetters("ccacbaba") # acb
    print Solution().removeDuplicateLetters("abacb") # abc

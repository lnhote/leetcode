class Solution(object):
    """docstring for Solution"""
    def isPalindrome(self, x):
        if x == 0:
            return True
        if  x < 0:
            return False
        end = 0
        tmp = x
        while tmp != 0:
            end = end + 1
            tmp = tmp/10
        start = 0
        end = end - 1
        while start <= end:
            if x/(10**start)%10 != x/(10**end)%10:
                return False
            start = start + 1
            end = end - 1
        return True

if __name__ == '__main__':
    print Solution().isPalindrome(123)
    print Solution().isPalindrome(-123)
    print Solution().isPalindrome(12321)
    print Solution().isPalindrome(-12321)
    print Solution().isPalindrome(1234554321)
    print Solution().isPalindrome(0)
        
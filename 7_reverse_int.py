class Solution(object):
    """docstring for Solution"""
    def reverse(self, x):
        result = 0
        maxint = 2**31-1
        minint = -(2**31-1)
        if x > maxint or x < minint:
            return 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        while x != 0:
            digit = x%10
            # print 'digit = ', digit, 'x = ', x, 'result = ', result
            if result <= ((maxint - digit)/10):
                result = result*10 + digit
                x = x/10
            else:
                return 0
            
        return result*sign 

# range [-(2**31-1), +(2**31-1)]       
if __name__ == '__main__':
    print Solution().reverse(123)
    print Solution().reverse(-123)
    print Solution().reverse(2**31-1)
    print Solution().reverse(-(2**31-1))
    print Solution().reverse(-(2**31))
    print Solution().reverse(2**31)
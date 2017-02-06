class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str2 = str.strip(' ')
        if len(str2) == 0:
            return 0
        sign = 1
        if str2[0] == '-':
            sign = -1
            str2 = str2[1:]
        elif str2[0] == '+':
            sign = 1
            str2 = str2[1:]
        if len(str2) == 0:
            return 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        result = 0
        for i in range(0, len(str2)):
            ch = str2[i]
            if ord(ch) >= ord('0') and ord(ch) <= ord('9'): #48-57
                digit = ord(ch) - ord('0')
                if sign == 1 and (result <= (INT_MAX - digit)/10): 
                    result = result*10 + sign*digit
                elif sign == -1 and (result >= (INT_MIN + digit)/10):
                    result = result*10 + sign*digit
                else:
                    if sign == 1:
                        return INT_MAX
                    else:
                        return INT_MIN
                if result > INT_MAX:
                    return INT_MAX
                elif result < INT_MIN:
                    return INT_MIN
            else:
                if result != 0:
                    break
                else:
                    return result 
        return result

if __name__ == '__main__':
    print Solution().myAtoi('123') #123
    print Solution().myAtoi('-123') #-123
    print Solution().myAtoi('123.1') #123
    print Solution().myAtoi('123asdf') #123
    print Solution().myAtoi('   123asdf   ') #123
    print Solution().myAtoi('   123a66asdf   ') #123
    print Solution().myAtoi('   ') #0
    print Solution().myAtoi('-') #0
    print Solution().myAtoi("  -0012a42") #-12
    print Solution().myAtoi("+-2") #0 
    print Solution().myAtoi("-2147483649")  #-2147483648
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = []
        for x in range(0,numRows):
            rows.append([])
        count = 0
        sign = True
        for i in range(0, len(s)):
            rows[count].append(s[i])
            if numRows == 1:
                continue
            if sign:
                if count == numRows - 1:
                    sign = not sign
                    count = count - 1
                else:
                    count = count + 1
            else:
                if count == 0:
                    sign = not sign
                    count = count + 1
                else:
                    count = count - 1

            # for j in range(0,numRows):
            #     print rows[j]
            # print '\n'
        return ''.join([''.join(row) for row in rows])

if __name__ == '__main__':
    print Solution().convert('PAYPALISHIRING',3) #PAHNAPLSIIGYIR
    print Solution().convert('ABCD',2) #ACBD
    print Solution().convert('ABC',2) #ACB
    print Solution().convert('ABC',1) #ACB
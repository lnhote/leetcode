class Solution(object):
    def hannoiOne(self, n, i1, i2):
        tower_list = ['A', 'B', 'C']
        print "move %s from %s to %s" % (n, tower_list[i1], tower_list[i2])

    def hannoi(self, n, i1, i2):
        if n == 1:
            self.hannoiOne(1, i1, i2)
        else:
            temp = 0
            if (i1 == 1 and i2 == 2) or (i1 == 2 and i2 == 1):
                temp = 0
            if (i1 == 1 and i2 == 0) or (i1 == 0 and i2 == 1):
                temp = 2
            if (i1 == 2 and i2 == 0) or (i1 == 0 and i2 == 2):
                temp = 1

            self.hannoi(n-1, i1, temp)
            self.hannoiOne(n, i1, i2)
            self.hannoi(n-1, temp, i2)

if __name__ == '__main__':
    Solution().hannoi(3, 0, 2)
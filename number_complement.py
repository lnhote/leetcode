class Solution(object):
	"""docstring for Solution"""
	def complement(self, num):
		result = 0
		pos = 0
		while num > 0:
		    result = result + (((num+1)&1)<<pos)
		    pos = pos + 1
		    num = num >> 1
		return result

if __name__ == '__main__':
    print Solution().complement(10)
    print Solution().complement(4)

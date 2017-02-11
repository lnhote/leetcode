class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        if len(s) == 0:
            return False
        for i in range(0, len(s)):
            if s[i] in ['(','[', '{']:
                stack.append(s[i])
            else:
                top = ''
                if len(stack) > 0:
                    top = stack.pop()
                if top == '(' and s[i] == ')':
                    continue
                if top == '[' and s[i] == ']':
                    continue
                if top == '{' and s[i] == '}':
                    continue
                return False
        if len(stack) == 0:
            return True
        else:
            return False
                

if __name__ == '__main__':
	print Solution().isValid('()') # True
	print Solution().isValid('()[]{}') # True
	print Solution().isValid('(]') # False
	print Solution().isValid('([)]') # False
	print Solution().isValid('') # False

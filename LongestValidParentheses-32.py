import sys
from copy import deepcopy

'''
Question: Given a string containing just 
the characters '(' and ')', find the length of 
the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses 
substring is "()", which has length = 2.

Another example is ")()())", where 
the longest valid parentheses substring is
 "()()", which has length = 4.
 
Solution: 
229 / 229 test cases passed.
Status: Accepted
Runtime: 146 ms

'''


class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type nums: str
		:rtype: int
		"""
		if len(s) < 2:
			return 0
 		stack = [s[0]]
		for i in range(1,len(s)):
			n = len(stack)
			if n >= 1:
				top = stack[n-1]
				if top == "(" and s[i] == ")":
					stack.pop()
					currentCount = 2
					while(len(stack) != 0):
						#print stack
						temp = stack.pop()
						if temp.isdigit() == True:
							currentCount += int(temp)
						else:
							stack.append(temp)
							break
					stack.append(str(currentCount))
					continue
				elif top.isdigit() and s[i] == ")":
					if n-2 >=0:
						temp = stack[n-2]
						if temp == "(":
							count = int(stack.pop())
							count += 2
							stack.pop()
							while len(stack) != 0 :
								temp = stack.pop()
								if temp.isdigit() == True:
									count += int(temp)
								else:
									stack.append(temp)
									break
							stack.append(str(count))
							continue
			stack.append(s[i])
		print stack
		globalMax = 0
		maxi = 0
		for s in stack:
			if s.isdigit():
				maxi += int(s)
			else:
				if globalMax < maxi:
					globalMax = maxi
				maxi = 0
		if maxi > globalMax:
		    return maxi
		else:
		    return globalMax


def main():
	a = ")(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))())"
	Sol = Solution()
	print Sol.longestValidParentheses(a)
	
	
	
if __name__ == "__main__":
    main()
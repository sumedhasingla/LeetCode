import sys
from copy import deepcopy

'''
Question: Given n pairs of parentheses, 
write a function to generate all combinations
 of well-formed parentheses.
 
Solution: 


'''


class Solution(object):
	def generateParenthesis(self, n):
		"""
		:type nums: int
		:rtype: List[str]
		"""
		return self.recursive(n,n,"") # we start with 3 left ((( and 3 right )))
	
	def recursive(self,left,right,string):
		if left == right and left == 0: # when there is no more left and right return the string
			return [string]
		if left == 0:
			return self.recursive(left,right-1,string+')') #when there is no more left, start appending right
		if left == right: #When they are equal, next must be a left, for valid combination
			return self.recursive(left-1,right,string+'(')
		else:
			one = self.recursive(left-1,right,string+'(') #try both options, putting next as left and right
			two = self.recursive(left,right-1,string+')')
			return one + two

def main():
	Sol = Solution()
	print Sol.generateParenthesis(3)
	
	
	
if __name__ == "__main__":
    main()
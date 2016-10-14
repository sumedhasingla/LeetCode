import sys
from copy import deepcopy

'''
Question: Given a set of distinct integers, 
nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

Solution: 10 / 10 test cases passed.
Status: Accepted
Runtime: 69 ms
'''


class Solution(object):
	def subsets(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		sol = [[]]
		for n in nums:
			currentSize = len(sol)
			for i in range(0,currentSize):
				temp = deepcopy(sol[i])
				temp.append(n)
				sol.append(temp)

		return sol


		
		
		
		
		
def main():
	a = [1,2,3]
	Sol = Solution()
	print Sol.subsets(a)
	
	
	
if __name__ == "__main__":
    main()
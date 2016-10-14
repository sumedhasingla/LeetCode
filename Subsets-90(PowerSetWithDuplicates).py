import sys
from copy import deepcopy

'''
Question:Given a collection of integers
 that might contain duplicates, nums, 
 return all possible subsets.

Note: The solution set must not contain d
uplicate subsets.

Solution: 19 / 19 test cases passed.
Status: Accepted
Runtime: 72 ms
'''


class Solution(object):
	def subsetsWithDup(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		sol = [[]]
		hashmap = {}
		for n in nums:
			currentSize = len(sol)
			for i in range(0,currentSize):
				temp = deepcopy(sol[i])
				temp.append(n)
				temp.sort()
				if hashmap.has_key(tuple(temp)):
					continue
				else:
					hashmap[tuple(temp)]=1
					sol.append(temp)

		return sol


		
		
		
		
		
def main():
	a = [1,2,2]
	Sol = Solution()
	print Sol.subsetsWithDup(a)
	
	
	
if __name__ == "__main__":
    main()
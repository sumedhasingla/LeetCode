import sys
from copy import deepcopy
import sets
'''
Question: Given a set of distinct positive integers, 
find the largest subset such that every pair (Si, Sj) 
of elements in this subset satisfies: Si % Sj = 0 or 
Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Solution: 32 / 32 test cases passed.
Status: Accepted
Runtime: 395 ms

'''

		

class Solution(object):
	def largestDivisibleSubset(self, nums):
		"""
		type type nums: List[int]
		:rtype: List[int]
		"""
		if len(nums) == 0:
			return nums
		numberSet = {}
		maxSize = 0
		maxSet = None
		nums.sort()
		for n in nums:
			numberSet[n] = set()  #Key is N, Value is an empty set
			maxSize1 = 0
			maxSize1Key = None
			for k in numberSet.keys():
				if n%k == 0 and len(numberSet[k]) >= maxSize1:   #Choose the max size subset as of now
					maxSize1 = len(numberSet[k])
					maxSize1Key = k
			if maxSize1Key != None:
				numberSet[n] = numberSet[n].union(numberSet[maxSize1Key]) #and append it
			numberSet[n].add(n)   #N set should have itself
			if len(numberSet[n]) > maxSize:
				maxSize = len(numberSet[n])
				maxSet = numberSet[n]
		return list(maxSet)

		
def main():
	a = [1,2,3]
	Sol = Solution()
	print Sol.largestDivisibleSubset(a)

	
	
	
if __name__ == "__main__":
    main()
import sys
from copy import deepcopy

'''
Question: Given a non-empty array containing only 
positive integers, find if the array can be partitioned 
into two subsets such that the sum of elements in 
both subsets is equal.

Note:
Both the array size and each of the array 
element will not exceed 100.
 
Solution: 

'''


class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		n = len(nums)
		if n < 2:
			return False
		nums.sort()
		forward = 1
		backward = n-2
		frontSum = nums[0]
		backSum = nums[backward+1]
		while forward < backward:
			if frontSum < backSum:
				frontSum += nums[forward]
				forward += 1
			elif frontSum > backSum:
				backSum += nums[backward]
				backward -= 1
			else:
				frontSum += nums[forward]
				forward += 1
				backSum += nums[backward]
				backward -= 1
		if forward == backward:
			if abs(frontSum - backSum) ==  nums[forward]:
				return True
		if frontSum == backSum:
			return True
		return False

def main():
	a = [1,1,1,1,1,1,1,2,3,2,3]
	Sol = Solution()
	print Sol.canPartition(a)
	
	
	
if __name__ == "__main__":
    main()
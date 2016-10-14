import sys
from copy import deepcopy

'''
Question: Given an unsorted array return 
whether an increasing subsequence of length
 3 exists or not in the array.

Solution: 
61 / 61 test cases passed.
Status: Accepted
Runtime: 62 ms


'''


class Solution(object):
	def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		n = len(nums)
		if n < 3:
			return False
		small = float("inf")
		smaller = float("inf")
		for i in range(0,n):
			if nums[i] <= smaller:
				smaller = nums[i]
			elif nums[i] <= small:  #number if bigger than "smaller" but smaller than "small"
				small = nums[i]
			else:
				return True
		return False
				
		
		
		

		
		
		
		
		
def main():
	a = [12,1,1,1,13,1,1,1,14]
	Sol = Solution()
	print Sol.increasingTriplet(a)
	
	
	
if __name__ == "__main__":
    main()
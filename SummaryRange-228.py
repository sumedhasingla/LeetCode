import sys
from copy import deepcopy

'''
Question: Given a sorted integer array without duplicates, 
return the summary of its ranges.

For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].

Solution: 27 / 27 test cases passed.
Status: Accepted
Runtime: 58 ms

'''


class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		sol = []
		if len(nums) == 0:
			return sol
		startRange = nums[0]
		endRange = nums[0]
		for i in range(1, len(nums)):
			if nums[i] == endRange+1:
				endRange = nums[i]
			else:
				if startRange == endRange:
					sol.append(str(startRange))
				else:
					sol.append(str(startRange) + "->" + str(endRange))
				startRange = nums[i]
				endRange = startRange
		if startRange == endRange:
			sol.append(str(startRange))
		else:
			sol.append(str(startRange) + "->" + str(endRange))
		return sol
		


		
		
		
		
		
def main():
	a = [0,1,2,4,5,7]
	Sol = Solution()
	print Sol.summaryRanges(a)
	
	
	
if __name__ == "__main__":
    main()
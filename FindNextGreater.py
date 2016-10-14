import sys
from copy import deepcopy

'''
Question: Given a number in the form of an array
find the next greater number that can be formed using the
digits of the array
 
Solution: 


'''


class Solution(object):
	def nextGreaterNumber(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		n = len(nums)
		if n <= 1:
			return nums
		index = n-2
		while index >= 0:
			if nums[index] > nums[index+1]:
				index -= 1
			else:
				tempArray = nums[index:]
				nums = nums[0:index]
				tempArray.sort()
				nums = nums + [tempArray.pop(1)] + tempArray
				break
				
		return nums

def main():
	a = [1,9,6,3,2]
	Sol = Solution()
	print Sol.nextGreaterNumber(a)
	
	
	
if __name__ == "__main__":
    main()
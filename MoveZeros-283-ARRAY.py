import sys

'''
Question:
Given an array nums, write a function to move all 0's to the 
end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your 
function, nums should be [1, 3, 12, 0, 0].

Solution:
21 / 21 test cases passed.
Status: Accepted
Runtime: 76 ms
'''



class Solution(object):
	def moveZeroesChangeOrder(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		backPointer = len(nums) - 1
		frontPointer = 0
		while frontPointer <= backPointer:
			if nums[frontPointer] != 0:
				frontPointer += 1
			else:
				while nums[backPointer] == 0:
					backPointer -= 1
				temp = nums[frontPointer]
				nums[frontPointer] = nums[backPointer]
				nums[backPointer] = temp
				backPointer -= 1
				frontPointer += 1
		
		return
		
	def moveZeroes(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		zeroIndex = -1
		for i in range(0,len(nums)):
			if nums[i] == 0:
				zeroIndex = i
				break
		if zeroIndex == -1:
			return
		for i in range(zeroIndex+1,len(nums)):
			if nums[i] != 0:
				nums[zeroIndex] = nums[i]
				zeroIndex += 1
		for i in range(zeroIndex,len(nums)):
			nums[i] = 0
		return


		
		
		
		
		
		
def main():
	a = [0,1,0,3,12]
	Sol = Solution()
	Sol.moveZeroes(a)
	print a
	
	
	
if __name__ == "__main__":
    main()
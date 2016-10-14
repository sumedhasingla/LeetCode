import sys
'''
##
##Question:
Given an array nums containing n + 1 integers where each integer 
is between 1 and n (inclusive), prove that at least one duplicate 
number must exist. Assume that there is only one duplicate number, 
find the duplicate one.


##53 / 53 test cases passed.
## Status: Accepted
## Runtime: 102 ms
'''


class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		index = 0
		while(nums[index] == index):
			index += 1
		
		temp = nums[index]
		nums[index] = -1
		index = temp
		
		
		while True:
			if index == nums[index] and nums[index] == -1:
				nums[index] = index
				index += 1
				while index == nums[index]:
					index += 1
				temp = nums[index]
				nums[index] = -1
				index = temp
			elif index == nums[index]:
				return index
			elif index != nums[index]:
				temp = nums[index]
				nums[index] = index
				index = temp
			
		
		
		
		
		
		
def main():
	a = [0,1,2,0,1]
	Sol = Solution()
	print Sol.findDuplicate(a)
	
	
	
if __name__ == "__main__":
    main()
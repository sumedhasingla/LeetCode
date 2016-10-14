import sys
from copy import deepcopy

'''
Question: Given an array which consists of non-negative 
integers and an integer m, you can split the array into 
m non-empty continuous subarrays. Write an algorithm to minimize 
the largest sum among these m subarrays.

Note:
Given m satisfies the following constraint: 
1 ≤ m ≤ length(nums) ≤ 14,000.

Solution:
28 / 28 test cases passed.
Status: Accepted
Runtime: 126 ms

'''


class Solution(object):
	def doable(self,nums,m,max):
		acc = 0 #sum of currently processed group
		for n in nums:
			if n > max:
				return False
			elif acc+n <= max: #if there is scope to add one more number to the group
				acc += n
			else:
				m -= 1 #we make a cut now. and create a new group with that element
				acc = n
				if m < 0: #no cuts left
					return False
		return True
		
		
	def splitArray(self, nums, m):
		"""
		:type nums: List[int]
		:type m: int
		:rtype: int
		"""
		left = max(nums) #the value of the largest element in this array.
		right = sum(nums) #sum of all elements in this array.
		
		#use binary search on these values to find the solution
		#solution lies between left and right, both included
		
		while left < right:
			middle = ( left + right )/2
			if self.doable(nums, m-1, middle):
				right = middle
			else:
				left = middle + 1
		return left



		
		
		
		
		
def main():
	a = [7,2,5,10,8]
	print Sol.splitArray(a,4)
	
	
	
if __name__ == "__main__":
    main()
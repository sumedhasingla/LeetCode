import sys

'''
Question: Given an array of n integers where n > 1, nums, 
return an array output such that output[i] is equal to the 
product of all the elements of nums except nums[i].

Solve it without division and in O(n).

Solution:
17 / 17 test cases passed.
Status: Accepted
Runtime: 206 ms
'''


class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""
		n = len(nums)
	
		zeroCount = 0
		zeroIndex = -1
		for i in range(0, n):
			if nums[i] == 0:
				zeroCount += 1
				zeroIndex = i
			if zeroCount > 1:
				sol = [0 for i in range(0,n)]
				return sol
		if zeroCount == 1:
			p = 1
			for i in range(0,n):
				if i == zeroIndex:
					continue
				p = p * nums[i]
			sol = [0 for i in range(0,n)]
			sol[zeroIndex] = p
			return sol
		#Now there is no zero in the array
		p = 1
		sol = [1 for i in range(0,n)]
		for i in range(0, n):
			sol[i] = sol[i] * p
			p = p * nums[i]
		p = 1
		for i in range(n-1,-1,-1):
			sol[i] = sol[i] * p
			p = p * nums[i]

		return sol


		
		
		
		
		
def main():
	a = [1,2,3,4]
	Sol = Solution()
	print Sol.productExceptSelf(a)
	
	
	
if __name__ == "__main__":
    main()
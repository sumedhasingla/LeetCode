import sys
from copy import deepcopy

'''
Question: Given an unsorted array of integers, 
find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], 
therefore the length is 4. Note that there may be more 
than one LIS combination, it is only necessary for you to 
return the length.

Your algorithm should run in O(n2) complexity.

Solution: 
23 / 23 test cases passed.
Status: Accepted
Runtime: 982 ms


'''


class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if n == 0:
			return 0
		if n == 1:
			return 1
		memory = [1 for i in range(0,n)]
		for i in range(1,n):
			for j in range(0,i):
				if nums[i] > nums[j] and memory[i] < memory[j]+1:
					memory[i] = memory[j] + 1
		return max(memory)


		
		
		
		
		
def main():
	word1 = "abcd"
	word2 = "dmob"
	Sol = Solution()
	print Sol.minDistance(word1,word2)
	
	
	
if __name__ == "__main__":
    main()
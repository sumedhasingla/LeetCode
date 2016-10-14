import sys
from copy import deepcopy

'''
Question: A sequence of numbers is called a wiggle 
sequence if the differences between successive numbers 
strictly alternate between positive and negative. 
The first difference (if one exists) may be either 
positive or negative. A sequence with fewer than two 
elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence 
because the differences (6,-3,5,-7,3) are alternately
 positive and negative. In contrast, [1,4,7,2,5] and 
 [1,7,4,5,5] are not wiggle sequences, the first because
 its first two differences are positive and the second
 because its last difference is zero.

Given a sequence of integers, 
return the length of the longest subsequence 
that is a wiggle sequence. 
A subsequence is obtained by deleting some number of
 elements (eventually, also zero) from the original 
 sequence, leaving the remaining elements in their 
 original order.
 
Solution: 
24 / 24 test cases passed.
Status: Accepted
Runtime: 69 ms

'''


class Solution(object):
	def wiggleMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if n <= 1:
			return n
		i = 1
		l = 1
		while i < n and nums[i] == nums[i-1]:
			i += 1
		if i == n:
			return l
		if nums[i-1]< nums[i]:
			next = False#small
		else:
			next = True#big
		prev = nums[i]
		l += 1
		
		for ii in range (i+1,n):
			if (next == False and nums[ii] < prev) or (next == True and nums[ii] > prev):
				next = not(next)#big
				prev = nums[ii]
				l += 1
			elif ( next == False and nums[ii] > prev ) or (next == True and nums[ii] < prev):
				prev = nums[ii]		
		return l

def main():
	a = [1,1,1,1,1,1,1,2,3,2,3]
	Sol = Solution()
	print Sol.wiggleMaxLength(a)
	
	
	
if __name__ == "__main__":
    main()
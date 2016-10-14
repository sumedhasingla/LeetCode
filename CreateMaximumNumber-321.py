import sys
from copy import deepcopy

'''
Question:Given two arrays of length m and n with 
digits 0-9 representing two numbers. 
Create the maximum number of length k <= m + n from 
digits of the two. The relative order of the digits 
from the same array must be preserved. Return an array 
of the k digits. You should try to optimize your time 
and space complexity.

Solution: 

'''


class Solution(object):
	def maxNumber(self, nums1, nums2, k):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:type k: int
		:rtype: List[int]
		"""
		temp1 = []
		temp2 = []
		for i in range(0,len(nums1)):
			temp1.append((nums1[i],i))
		for i in range(0,len(nums2)):
			temp2.append((nums2[i],i))

		temp1.sort()
		temp2.sort()
		
		sortIndex1 = len(temp1)-1
		sortIndex2 = len(temp2)-1
		sol = []
		while len(sol)!=k:
			if temp1[sortIndex1][0] > temp2[sortIndex2][0]:
				maxIndex = temp1[sortIndex1][1]
				
		
				
		return 


		
		
		
		
		
def main():
	a = [9,8,9]
	b = [3,9]
	Sol = Solution()
	print Sol.maxNumber(a,b,3)
	
	
	
if __name__ == "__main__":
    main()
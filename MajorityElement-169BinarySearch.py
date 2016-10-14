import sys
from copy import deepcopy

'''
Question: Given an array of size n, find the majority element. 
The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority 
element always exist in the array.
 
Solution: 44 / 44 test cases passed.
Status: Accepted
Runtime: 185 ms


'''


class Solution(object):
	def majorityElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		temp ={}
		sol = self.search(0,len(nums)-1,temp,nums)
		return sol
	
	def search(self,start,end,count,nums):
		if start <= end:
			middle = int((start+end)/2)
			if count.has_key(nums[middle]):
				count[nums[middle]] = count[nums[middle]] + 1
			else:
				count[nums[middle]] = 1
			if count[nums[middle]] > int(len(nums)/2):
					return nums[middle]
			sol1 = self.search(start,middle-1,count,nums)
			if sol1 != None:
				return sol1
			sol2 = self.search(middle+1,end,count,nums)
			if sol2 != None:
				return sol2
		return None


def main():
	a = [1,1,1,1,1,1,1,2,3,2,3]
	Sol = Solution()
	print Sol.majorityElement(a)
	
	
	
if __name__ == "__main__":
    main()
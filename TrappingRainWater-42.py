import sys
from copy import deepcopy

'''
Question: Given n non-negative integers representing an 
elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Solution: correct but time complexity is high

'''


class Solution(object):
	def trap(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		n = len(height)
		sol = 0
		
		bucketSize = 3
		while bucketSize <= n:
			for i in range(0, n - bucketSize + 1):
				minWater = min(height[i], height[i+bucketSize -1])
				if minWater <= 0:
					continue
				maxWater = max(height[i+1:i+bucketSize-1])
				addWater = minWater - maxWater
				if addWater > 0:
					for j in range(i+1, i + bucketSize-1):
						height[j] += addWater
						sol += addWater
			bucketSize += 1

		return sol


		
		
		
		
		
def main():
	a = [0,1,0,2,1,0,1,3,2,1,2,1]
	Sol = Solution()
	print Sol.trap(a)
	
	
	
if __name__ == "__main__":
    main()
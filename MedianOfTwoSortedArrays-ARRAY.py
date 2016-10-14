import sys

'''
Question: here are two sorted arrays nums1 and nums2
of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n))..

Solution: 

'''


class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums1: List[int]
		:rtype: float
		"""
		
		start1 = 0
		start2 = 0
		end1 = len(nums1)-1
		end2 = len(nums2)-1
		while True:
			count1 = len(nums1)
			count2 = len(nums2)
			isEven1 = False
			isEven2 = False
			if count1%2 == 0:
				median1 = float((nums1[int(count1/2)] + nums1[int(count1/2)-1])/2)
				isEven1 = True
			else:
				median1 = nums1[int(count1/2)]
			if count2%2 == 0:
				median2 = float((nums2[int(count2/2)] + nums2[int(count2/2)-1])/2)
				isEven2 = True
			else:
				median2 = nums2[int(count2/2)]
			if median1 == median2:
				return median1
			if count1 > 2 and count2 > 2:
				if median1 > median2:
					if isEven1:
						nums = nums1[:int(count1/2)]
					else:
						nums1 = nums1[:int(count1/2)+1]
					nums2 = nums2[int(count2/2):]
				else:
					nums1 = nums1[int(count1/2):]
					if isEven2:
						nums2 = nums2[:int(count2/2)]
					else:
						nums2 = nums2[:int(count2/2)+1]
				print nums1
				print nums2
				print ",,,,,,,,,,,,,,,"
			else:
				break
				
		nums1 = nums1 + nums2
		nums1.sort()
		count = len(nums1)
		if count%2 == 0:
			return float((nums1[int(count/2)] + nums1[int(count/2)-1])/2)
		else:
			return nums1[int(count/2)]
			
				
		
				
			
				


		
		
		
		
		
def main():
	a = [1,3,3,4,5]
	b = [2,3,4,5,6,7]
	Sol = Solution()
	print Sol.findMedianSortedArrays(a,b)
	
	
	
if __name__ == "__main__":
    main()
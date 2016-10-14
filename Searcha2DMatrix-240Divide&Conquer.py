import sys
from copy import deepcopy

'''
Question: Write an efficient algorithm that searches for a value 
in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
 a: Smaller than X
 b: bigger than X
 
 [a,    a,    a, (a,b), (a,b)]
 [a,    a,    a, (a,b), (a,b)]
 [a,    a,    X,   b,     b  ]
 [(a,b) (a,b) b,   b,     b  ]
 [(a,b) (a,b) b,   b,     b  ]
 
Solution: 127 / 127 test cases passed.
Status: Accepted
Runtime: 645 ms


'''


class Solution(object):
	def searchMatrix(self, matrix, target):
		"""
		:type matrix: List[List[int]]
		:type target: int
		:rtype: bool
		"""
		def search(minRow,minCol,maxRow,maxCol):
			if minRow == maxRow and minCol == maxCol: #Only one element
				if matrix[minRow][minCol] == target:
					return True
				else:
					return False
			if minRow <= maxRow and minCol <= maxCol:
				middleRow = int((minRow+maxRow)/2)
				middleCol = int((minCol+maxCol)/2)
				if matrix[middleRow][middleCol] == target:
					return True
				if matrix[middleRow][middleCol] < target:
					temp = search(minRow,middleCol+1,maxRow,maxCol)
					if temp == True:
						return temp
					temp = search(middleRow+1,minCol,maxRow,middleCol)
					if temp == True:
						return temp
				else:
					temp = search(minRow,minCol,maxRow,middleCol-1)
					if temp == True:
						return temp
					temp = search(minRow,middleCol,middleRow-1,maxCol)
					if temp == True:
						return temp
			return False
		return search(0,0,len(matrix)-1,len(matrix[0])-1)
	

def main():
	a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
	Sol = Solution()
	print Sol.searchMatrix(a,11)
	
	
	
if __name__ == "__main__":
    main()
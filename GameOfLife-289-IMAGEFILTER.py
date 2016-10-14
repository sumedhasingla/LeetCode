import sys
from copy import deepcopy

class Solution(object):
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		rows = len(board)
		cols = len(board[0])
		hashMap = {}
		for i in range(0,rows):
			for j in range(0, cols):
				rowStart = i - 1
				rowEnd = i + 1
				colStart = j -1
				colEnd = j + 1
				if rowStart < 0:
					rowStart = 0
				if colStart < 0:
					colStart  = 0
				if rowEnd >= rows:
					rowEnd = rows - 1
				if colEnd >= cols:
					colEnd = cols - 1
				liveN = 0
				for ii in range(rowStart,rowEnd+1):
					for jj in range(colStart,colEnd+1):
						if board[ii][jj] == 1:
							liveN += 1
						if liveN == 5:
							break
				newValue = 1
				if board[i][j] == 1:
					liveN -= 1
					if liveN < 2 or liveN > 3:
						newValue = 0
				else:
					if liveN != 3:
						newValue = 0
				hashMap[(i,j)] = newValue
		
		for i in range(0,rows):
			for j in range(0, cols):
				board[i][j] = hashMap[(i,j)]
		
		
		return
		

	
		
		
		
		
		
def main():
	a = [[1,0,1], [0,0,1], [1,0,0]]
	Sol = Solution()
	Sol.gameOfLife(a)
	print a
	
	
if __name__ == "__main__":
    main()
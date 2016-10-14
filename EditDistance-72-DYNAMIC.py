import sys
from copy import deepcopy

'''
Question: Given two words word1 and word2,
 find the minimum number of steps required to
 convert word1 to word2. 
 (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character

Solution: 1146 / 1146 test cases passed.
Status: Accepted
Runtime: 285 ms

'''


class Solution(object):
	def minDistance(self, word1, word2):
		"""
		:type word1: str
		:type word2: str
		:rtype: int
		"""
		sol = 0
		
		rows = len(word1)
		cols = len(word2)
		
		#temp memory for dynamic programming
		D = [ [None for i in range(0,cols+1)] for i in range(0,rows+1) ]
		D[0][0] = 0
		for i in range(0,rows+1):
			D[i][0] = i
		for i in range(0,cols+1):
			D[0][i] = i
		for i in range(1,rows+1):
			for j in range(1,cols+1):
				if word1[i-1] == word2[j-1]:
					subCost = D[i-1][j-1]
				else:
					subCost = D[i-1][j-1]+1
				insertCost = D[i][j-1] + 1
				deletionCost = D[i-1][j] + 1
				D[i][j] = min(subCost,insertCost,deletionCost)
		#print D
		
		
		
		
		

		return D[rows][cols]


		
		
		
		
		
def main():
	word1 = "abcd"
	word2 = "dmob"
	Sol = Solution()
	print Sol.minDistance(word1,word2)
	
	
	
if __name__ == "__main__":
    main()
import sys
from copy import deepcopy

'''
Question: Given a string S and a string T, count 
the number of distinct subsequences of T in S.

A subsequence of a string is a new string which 
is formed from the original string by deleting some 
(can be none) of the characters without disturbing the relative positions of the
 remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Solution: 
63 / 63 test cases passed.
Status: Accepted
Runtime: 348 ms



'''


class Solution(object):
	def numDistinct(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: int
		"""
		
		rows = len(t)
		cols = len(s)
		
		memory = [[0 for j in range(0,cols+1)]for i in range(0,rows+1)]
		for j in range(0,cols+1):
			memory[0][j] = 1   #When target is "" result is always 1
		
		for i in range(1,rows+1):
			for j in range(1,cols+1):
				if t[i-1] == s[j-1]: 
					memory[i][j] = memory[i-1][j-1]
				memory[i][j] += memory[i][j-1] #when the current alphabets don't match, ans is same as if source don't have this new alphabet
				
		return memory[rows][cols]


		
		
		
		
		
def main():
	word1 = "amnaqarbocbmc"
	word2 = "abc"
	Sol = Solution()
	print Sol.numDistinct(word1,word2)
	
	
	
if __name__ == "__main__":
    main()
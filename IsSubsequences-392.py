import sys
from copy import deepcopy

'''
Question: Given a string s and a string t, check if s
is subsequence of t.

You may assume that there is only lower case 
English letters in both s and t. t is potentially a very long 
(length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed 
from the original string by deleting some (can be none) of the 
characters without disturbing the relative positions of the remaining 
characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Solution: 13 / 13 test cases passed.
Status: Accepted
Runtime: 388 ms



'''


class Solution(object):
	def isSubsequence(self, s, t):
		"""
		:type s: str small string
		:type t: str long continuous stream
		:rtype: bool
		"""
		
		indexS = 0
		indexT = 0
		while indexT < len(t):
			if indexS < len(s):
				if s[indexS] == t[indexT]:
					indexS += 1
			else:
				return True
			indexT += 1
			
		if indexT == len(t) and indexS == len(s):
		    return True
		return False

		
		
		
		
		
def main():
	word1 = "amnaqarbocbmc"
	word2 = "abc"
	Sol = Solution()
	print Sol.numDistinct(word1,word2)
	
	
	
if __name__ == "__main__":
    main()
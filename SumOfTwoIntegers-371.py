import sys
from copy import deepcopy

'''
Question: Calculate the sum of two integers a and b, 
but you are not allowed to use the operator + and -.
 
Solution: 


'''


class Solution(object):
	def getSum(self, a, b):
		"""
		:type a: int
		:type b: int
		:rtype: int
		"""
		if a < 0:
			a = ~abs(a) + 1
		if b < 0:
			b = ~abs(b) + 1
		mask = 1
		sol = []
		cary = 0
		while a != 0 and b != 0:
			tempA = a & mask
			tempB = b & mask
			if cary == 1:
				if tempA != tempB:
					currentBit = 0
					cary = 1
				else:
					currentBit = 1
					cary = tempA
			else:
				if tempA != tempB:
					currentBit = 1
				else:
					currentBit = 0
					cary = tempA
			sol.insert(0,str(currentBit))
			a = a >> 1
			b = b >> 1
		if a == 0 and b !=0:
			while b != 0:
				tempB = b & mask
				if cary == 1 and tempB == 1:
					currentBit = 0
					cary = 1
				elif cary == 1 and tempB == 0:
					currentBit = 1
					cary = 0
				elif cary == 0:
					currentBit = tempB
				sol.insert(0,str(currentBit))
				b = b >> 1
		if b == 0 and a !=0:
			while a != 0:
				tempA = a & mask
				if cary == 1 and tempA == 1:
					currentBit = 0
					cary = 1
				elif cary == 1 and tempA == 0:
					currentBit = 1
					cary = 0
				elif cary == 0:
					currentBit = tempA
				sol.insert(0,str(currentBit))
				a = a >> 1
		sol.insert(0,str(cary))
		return int("".join(sol),2)
					
def main():
	Sol = Solution()
	print Sol.getSum(1,-1)
	
	
	
if __name__ == "__main__":
    main()
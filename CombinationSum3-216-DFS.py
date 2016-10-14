import sys
from copy import deepcopy

'''
Question: Find all possible combinations of k 
numbers that add up to a number n, given that only 
numbers from 1 to 9 can be used and each combination 
should be a unique set of numbers.

Solution: 18 / 18 test cases passed.
Status: Accepted
Runtime: 105 ms

'''
class Node(object):
	def __init__(self, state, path, k, n):
		self.state = state
		self.path = path
		self.k = k
		self.n = n
	
	def goalTest(self):
		if len(self.path) == self.k +1 and sum(self.path) == self.n:
			return True
		else:
			return False
	
	def getSuccessorStates(self):
		outputStates = []
		for i in range(self.state+1,10):
			if not( i in self.path ):
				if len(self.path) <= self.k + 1 and sum(self.path) + i <= self.n:
					outputStates.append(i)
		#print "Input:" , self.state, "CurrentPath:", self.path,"Output:" , outputStates
		return outputStates
		

class Solution(object):
	def combinationSum3(self, k, n):
		"""
		type k: int
		:type n: int
		:rtype: List[List[int]]
		"""
		sol = []
		if n < k * (k+1)/2:
			return sol
		root = Node(0,[0],k,n)
		Frontier = []
		Frontier.append(root)
		while True:
			if len(Frontier) == 0:
				return sol
			parent = Frontier.pop()
			if parent.goalTest():
				currentSol = parent.path[1:]
				#currentSol.sort()
				#if not(currentSol in sol):
				sol.append(currentSol)
			outputStates = parent.getSuccessorStates()
			for state in outputStates:
				newPath = deepcopy(parent.path)
				newPath.append(state)
				node = Node(state,newPath,k,n)
				Frontier.append(node)

		
def main():
	Sol = Solution()
	print Sol.combinationSum3(6,35)

	
	
	
if __name__ == "__main__":
    main()
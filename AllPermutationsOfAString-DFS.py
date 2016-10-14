import sys
from copy import deepcopy

'''
Question: Find all possible permutations of a given string

Solution: 

'''
class Node(object):
	def __init__(self, state, path, inputString):
		self.state = state
		self.path = path
		self.inputString = inputString
	
	def goalTest(self):
		if len(self.path) == len(self.inputString) + 1:
			return True
		else:
			return False
	
	def getSuccessorStates(self):
		outputStates = []
		for a in self.inputString:
			if not( a in self.path ):
				if len(self.path) <= len(self.inputString)+ 1:
					outputStates.append(a)
		#print "Input:" , self.state, "CurrentPath:", self.path,"Output:" , outputStates
		return outputStates
		

class Solution(object):
	def allPermutations(self, inputString):
		"""
		type inputString: str
		:rtype: List[str]
		"""
		sol = []
		root = Node(0,[0], inputString)
		Frontier = []
		Frontier.append(root)
		while True:
			if len(Frontier) == 0:
				return sol
			parent = Frontier.pop()
			if parent.goalTest():
				currentSol = parent.path[1:]
				sol.append(''.join(currentSol))
			outputStates = parent.getSuccessorStates()
			for state in outputStates:
				newPath = deepcopy(parent.path)
				newPath.append(state)
				node = Node(state,newPath,inputString)
				Frontier.append(node)

		
def main():
	Sol = Solution()
	print len(Sol.allPermutations("abcd"))

	
	
	
if __name__ == "__main__":
    main()
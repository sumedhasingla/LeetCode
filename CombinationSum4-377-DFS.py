import sys
from copy import deepcopy

'''
Question: Given an integer array with all positive 
numbers and no duplicates, find the number of possible 
combinations that add up to a positive integer target.

Solution: Correct but not in time

'''
class Node(object):
	def __init__(self, state, path):
		self.state = state
		self.path = path
	
	def goalTest(self,target):
		if sum(self.path) == target:
			return True
		else:
			return False
	
	def getSuccessorStates(self,nums,target):
		outputStates = []
		for i in nums:
			if sum(self.path) + i <= target:
				outputStates.append(i)
		#print "Input:" , self.state, "CurrentPath:", self.path,"Output:" , outputStates
		return outputStates
		

class Solution(object):
	def combinationSum4(self, nums, target):
		"""
		type nums: List[int]
		:type target: int
		:rtype: int
		"""
		sol = 0
		root = Node(0,[0])
		Frontier = []
		Frontier.append(root)
		while True:
			if len(Frontier) == 0:
				return sol
			parent = Frontier.pop()
			if parent.goalTest(target):
				sol += 1
			outputStates = parent.getSuccessorStates(nums,target)
			for state in outputStates:
				newPath = deepcopy(parent.path)
				newPath.append(state)
				node = Node(state,newPath)
				Frontier.append(node)

		
def main():
	a = [1, 2, 3]
	Sol = Solution()
	print Sol.combinationSum4(a,4)

	
	
	
if __name__ == "__main__":
    main()
import sys
from copy import deepcopy

'''
Question: A frog is crossing a river. The river is divided into x units
 and at each unit there may or may not exist a stone. 
 The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, 
determine if the frog is able to cross the river by landing on the 
last stone. Initially, the frog is on the first stone and assume the 
first jump must be 1 unit.

If the frog's last jump was k units, then its next jump must be 
either k - 1, k, or k + 1 units. 
Note that the frog can only jump in the forward direction.

Note:

The number of stones is >= 2 and is < 1,100.
Each stone's position will be a non-negative integer < 231.
The first stone's position is always 0.

Solution: 
39 / 39 test cases passed.
Status: Accepted
Runtime: 62 ms
96.75%...

'''




class Node(object):
	def __init__(self, state,parentStepSize ):
		self.state = state
		self.parentStepSize = parentStepSize

	
	def goalTest(self,goalState):
		#print goalState
		if self.state == goalState:
			return True
		else:
			return False
	
	def getSuccessorStates(self,goalState):
		outputStates = []
		for i in range(-1,2):
			newState = self.state + self.parentStepSize + i
			if newState != self.state and newState <= goalState:
				outputStates.append([newState, self.parentStepSize+i])
		#print "Input:" , self.state, "Output:" , outputStates
		return outputStates
		

class Solution(object):
	def canCross(self, stones):
		"""
		type stones: List[int]
		:rtype: bool
		"""
		stoneHashMap = {}
		if stones[0] != 0 or stones[1] != 1:
			return False
		for i in range(0,len(stones)):
			if not(i == 0 or i == 1 or i == 2):
				if stones[i] > stones[i-1]*2:
					return False
			stoneHashMap[stones[i]] = 1
		
		goalState = stones[len(stones)-1]
		
		root = Node(1,1)
		Frontier = []
		Frontier.append(root)
		while True:
			if len(Frontier) == 0:
				return False
			parent = Frontier.pop()
			if parent.goalTest(goalState):
				return True
			outputStates = parent.getSuccessorStates(goalState)
			for state in outputStates:
				if stoneHashMap.has_key(state[0]):
					node = Node(state[0],state[1])
					Frontier.append(node)


		
def main():
	a = [0,1,3,4,5,7,9,10,12]
	Sol = Solution()
	print Sol.canCross(a)

	
	
	
if __name__ == "__main__":
    main()
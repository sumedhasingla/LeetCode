import sys

class Solution(object):
	def maxRotateFunction(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		Max = self.calculateFunctionValue(A)
		for i in range(1,len(A)):
			newA = A[len(A)-i:len(A)+1] + A[0:len(A)-i]
			m = self.calculateFunctionValue(newA)
			print newA
			if m > Max:
				Max = m
		return Max

		
	def calculateFunctionValue(self,A):
		ans = 0
		for i in range(0,len(A)):
			ans += i * A[i]
		return ans
		
	def easy(self,A):
		Max = 0
		SumAll = 0
		for i in range(0, len(A)):
			Max += i * A[i]
			SumAll += A[i]
		
		M = Max
		for i in range(1,len(A)):
			M = M - SumAll + len(A) * A[i-1]
			if M > Max:
				Max = M
		return Max
		
		
		
		
		
		
def main():
	a = [5,2,-1,-5,12,-5]
	Sol = Solution()
	print Sol.maxRotateFunction(a)
	
	
	
if __name__ == "__main__":
    main()
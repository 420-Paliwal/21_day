class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if (n<=0):
            return 
        self.printNumbers(n-1)
        print(n)

class Solution:
    def printNumbers(self, n):
        # Your code goes here
        if(n<=0):
            return
        print(n)
        self.printNumbers(n-1)
    
class Solution:
    def NnumbersSum(self, N):
        #your code goes here
        if(N<=0):
            return 0
        return N + self.NnumbersSum(N-1)

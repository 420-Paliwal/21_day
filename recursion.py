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
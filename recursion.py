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

class Solution:
    def factorial(self, n):
        if (n<= 1):
            return 1
        return n*self.factorial(n-1)

class Solution:
    def reverse(self, arr: list, n: int) -> None:
        low = 0
        high = n-1
        def rev_arr(arr, low, high):
            if (low >= high):
                return arr
            arr[low], arr[high] = arr[high], arr[low]
            rev_arr(arr, low+1, high-1)
        return rev_arr(arr, low, high)

class Solution:    
    def palindromeCheck(self, s):
        #your code goes here
        low = 0
        n = len(s)
        high = n-1
        def check(s, low, high):
            if(low>high):
                return True
            if(s[low] != s[high]):
                return False
            return check(s, low+1, high-1)
        return check(s, low, high)
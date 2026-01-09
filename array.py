class Solution:
    def countDigit(self, n):
        count = 0 
        while(n>0):
            count += 1 
            n = n// 10
        return count
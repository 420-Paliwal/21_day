class Solution:
    def countDigit(self, n):
        count = 0 
        while(n>0):
            count += 1 
            n = n// 10
        return count

class Solution:
    def reverseNumber(self, n):
        rev_num = 0
        while (n > 0):
            ld = n%10
            n = n//10
            rev_num = (rev_num * 10) + ld
        return rev_num
    

class Solution:
    def isPalindrome(self, n):
        temp = n
        rev_num = 0
        while(n>0):
            ld = n%10
            n = n//10
            rev_num = (rev_num *10) + ld
        return temp == rev_num
    
class Solution:
    def isArmstrong(self, n):
        arm = 0
        temp = n 
        while(n > 0):
            ld = n%10
            n = n//10
            arm += ld*ld*ld
        return temp == arm
    
import math
class Solution:
    def divisors(self, n):
        temp = []
        for i in range(1,int(math.sqrt(n))+1):
            if n%i == 0:
                temp.append(i)
                if n//i != i:
                    temp.append(n//i)
        temp.sort()
        return temp
    
import math
class Solution:
    def isPrime(self, n):
        #your code goes here
        if n <= 1:
            return False 

        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        return True
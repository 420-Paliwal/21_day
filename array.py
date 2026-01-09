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
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x    
        rev = 0
        while temp > 0 :    
            last_digit = temp%10
            rev = rev*10 + last_digit
            temp = temp//10   
        if  x == rev:
            return True
        return False       
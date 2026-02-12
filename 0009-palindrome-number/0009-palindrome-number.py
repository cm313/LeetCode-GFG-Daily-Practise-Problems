class Solution:
    def isPalindrome(self, x: int) -> bool:
        s_x = ""
        if x < 0:
            return False
        str_x = str(x)  
        n = len(str_x)  
        for i in range(n):
            s_x += str_x[n-i-1]    
        if str_x == s_x:
            return True
        else:
           return False        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        palin = ""
        n = len(str_x)
        for i in range(n):
            palin += str_x[n-i-1]
        res = int(palin)    
        if x == res:
            return True
        return False        
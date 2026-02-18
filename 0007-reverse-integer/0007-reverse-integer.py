class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            temp = -1*x   
        else:
            temp = x     
        rev = 0
        while temp > 0:    
            last_digit = temp%10
            rev = rev*10 + last_digit
            temp = temp//10  
        if x < 0:
            rev = -1*rev
        calc = math.pow(2,31)
        if rev > (-1*calc) and rev < (calc-1):
            return rev
        else:
            return 0
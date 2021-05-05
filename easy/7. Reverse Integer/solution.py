class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:  # handle positive numbers  
            a =  int(str(x)[::-1])  
        elif x <=0:  # handle negative numbers  
            a = -int(str(-x)[::-1])  
        # handle 32 bit overflow  
        mina = -2**31  
        maxa = 2**31 - 1  
        if a > maxa or a < mina:  
            return 0  
        else:  
            return a
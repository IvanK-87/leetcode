class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        sum_r = 0
        sum_l = 0
        sum_pair = 0

        for i in s:
            if i == '(':
                sum_r+=1
            if i == ')':
                sum_l+=1
                if sum_r>0:
                    sum_r-=1
                    sum_pair+=1

        return sum_r+sum_l-sum_pair
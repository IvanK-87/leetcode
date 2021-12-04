class Solution:
    def minDifference(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 4:
            return 0
        min_val = inf
        max_val = -inf
        tmp_lst = [inf]*4 + [-inf]*4
        for i in nums:
            if i > tmp_lst[4]:            
                if i > tmp_lst[7]:
                    tmp_lst[4] = tmp_lst[5]
                    tmp_lst[5] = tmp_lst[6]
                    tmp_lst[6] = tmp_lst[7]
                    tmp_lst[7] = i
                elif i > tmp_lst[6]:
                    tmp_lst[4] = tmp_lst[5]
                    tmp_lst[5] = tmp_lst[6]
                    tmp_lst[6] = i
                elif i > tmp_lst[5]:
                    tmp_lst[4] = tmp_lst[5]
                    tmp_lst[5] = i
                else:
                    tmp_lst[4] = i
                    
            if i < tmp_lst[3]:
                if i < tmp_lst[0]:
                    tmp_lst[3] = tmp_lst[2]
                    tmp_lst[2] = tmp_lst[1]
                    tmp_lst[1] = tmp_lst[0]
                    tmp_lst[0] = i
                elif i < tmp_lst[1]:
                    tmp_lst[3] = tmp_lst[2]
                    tmp_lst[2] = tmp_lst[1]
                    tmp_lst[1] = i
                elif i < tmp_lst[2]:
                    tmp_lst[3] = tmp_lst[2]
                    tmp_lst[2] = i
                else:
                    tmp_lst[3] = i


        min_val = inf
        for i in range(4):
            min_val = min(min_val, tmp_lst[4 + i] - tmp_lst[i])
        return min_val
        

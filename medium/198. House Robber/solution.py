class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l <= 2:
            return max(nums)
        else:
            max_money = [0]*l
            max_money[0] = nums[0]
            max_money[1] = max(nums[0], nums[1])
            for i in range(2, l):
                max_money[i] = max(max_money[i-1], max_money[i-2] + nums[i])
                
            return max_money[-1]
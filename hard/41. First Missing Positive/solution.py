class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)+1
        if N == 1: return 1

        nums.insert(0,0)
        for i in reversed(range(1,N)):
            num = nums[i]
            if i<=num or num<=0: continue
            #elif num<=0 or num>i: continue

            for j in range(i):
                tmp = nums[num]
                nums[num] = num
                num = tmp
                #nums[num],num = num,nums[num] 
                if num<=0 or num>i or num == nums[num]: break

        for i in range(1,N): 
            if nums[i] != i: return i
        return N
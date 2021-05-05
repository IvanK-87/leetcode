class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums = nums + [0]
        nums.sort()
        n = len(nums)

        double_val = 0
        missing_val = n-1
        for i in range(1, n):
            if nums[i-1] == nums[i]:
                double_val = nums[i]
            elif nums[i] - nums[i-1] > 1:
                missing_val = nums[i] - 1

        return([double_val, missing_val])
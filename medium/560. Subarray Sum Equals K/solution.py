class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        cur_sum = n = 0
        for i in nums:
            cur_sum += i
            tmp = sums[cur_sum - k]
            if tmp:
                n += tmp
            sums[cur_sum] += 1

        return n
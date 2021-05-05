class Solution:
    @functools.lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n<=3: return n
        k = n//2
        return (self.climbStairs(k)*self.climbStairs(n-k) + \
                self.climbStairs(k-1)*self.climbStairs(n-k-1))
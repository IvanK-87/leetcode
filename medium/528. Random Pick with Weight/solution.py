class Solution:
    def __init__(self, w: List[int]):
        self.sum = sum(w)
        self.n = len(w)
        self.interval = [sum(w[:i]) for i in range(1, self.n + 1, 1)]

    def pickIndex(self) -> int:
        seed = random.randint(1, self.sum)
        
        if seed <= self.interval[0]:
            return 0
        
        left = 0
        right = self.n - 1
        
        while left != right - 1:
            mid = (left + right) // 2
            
            if self.interval[mid] == seed:
                return mid
            
            if self.interval[mid] < seed:
                left = mid
            else:
                right = mid
            
        return right
    
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
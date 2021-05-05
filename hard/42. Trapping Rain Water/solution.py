class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        maxh = max(height)
        sumh = sum(height)
        
        tmp = [0]*n
        prev_max = 0
        for i in range(0, n):
            h = height[i]
            prev_max = max(h, prev_max)
            white = maxh - prev_max 
            if h > h_prev:
                tmp[i] = h
            else:
                tmp[i] = h+1
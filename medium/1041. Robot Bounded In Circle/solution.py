class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        state_lst = ((0,1), (1,0), (0,-1), (-1,0))
        step = {'L': 3,
               'R': 1}
        n = 0
        vx, vy = state_lst[n]
        x0 = y0 = 0
        for s in instructions:
            if s == 'G':
                x0 += vx
                y0 += vy
            else:
                n = (n + step[s]) % 4
                vx, vy = state_lst[n]
        
        if n == 0 and (x0 != 0 or y0 != 0):
            return False
        return True
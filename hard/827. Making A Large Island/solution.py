class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        grd0 = [[0]*(n+2)]
        grd1 = [[0]+i+[0] for i in grid]
        grd2 = [[0]*(n+2)]

        
        grd = grd0 + grd1 + grd2
        
        def mark_island(grd, i, j, mark):
            s = 0
            cells = deque()
            cells.append((i, j))
            nulls = set()
            
            while True:
                try:
                    ii, jj = cells.popleft()
                    if grd[ii][jj] == 1:
                        s += 1
                        grd[ii][jj] = mark
                        for nx, ny in ((ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)):
                            if grd[nx][ny] == 1:
                                cells.append((nx, ny))
                            elif grd[nx][ny] < 1:
                                nulls.add((nx, ny))

                except Exception:
                    for ii, jj in nulls:
                        grd[ii][jj] -= s
                    return
                    
        mark = 1
        for i in range(1, n+1):
            tmp = grd[i]
            for j in range(1, n+1):
                if tmp[j] == 1:
                    mark += 1
                    mark_island(grd, i, j, mark)
        
        answer = 1
        answer -= min([min(l) for l in grd])
        
        
        return min(n*n, answer)

 
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        l1 = len(A)
        l2 = len(A[0])
        l1_minus = l1 - 1
        l2_minus = l2 - 1

        def get_start_point(A, l1, l2):
            for i in range(l1):
                for j in range(l2):
                    if A[i][j] == 1:
                        return i, j
                    
        min_i, jj = get_start_point(A, l1, l2)
        A[min_i][jj] = 2
        d1 = deque()        
        d1.append((min_i, jj, min_i+1, l1_minus, 0, l2_minus))
        d2 = deque()

        while len(d1) > 0:
                ii, jj, imin, imax, jmin, jmax = d1.popleft()

                if jj > jmin:
                    ndx = jj - 1
                    if A[ii][ndx] == 1:
                        A[ii][ndx] = 2
                        d1.append((ii, ndx, min_i, l1_minus, 0, ndx))
                    elif A[ii][ndx] == 0:
                        d2.append((ii, ndx, min_i, l1_minus, 0, ndx))
                        
                if jj < jmax:
                    ndx = jj + 1
                    if A[ii][ndx] == 1:
                        A[ii][ndx] = 2
                        d1.append((ii, ndx, min_i, l1_minus, ndx, l2_minus))
                    elif A[ii][ndx] == 0:
                        d2.append((ii, ndx, min_i, l1_minus, ndx, l2_minus))


                if ii > imin:
                    ndx = ii - 1
                    if A[ndx][jj] == 1:
                        A[ndx][jj] = 2
                        d1.append((ndx, jj, min_i, ndx, 0, l2_minus))
                    elif A[ndx][jj] == 0:
                        d2.append((ndx, jj, min_i, ndx, 0, l2_minus))
                        
                if ii < imax:
                    ndx = ii + 1
                    if A[ndx][jj] == 1:
                        A[ndx][jj] = 2
                        d1.append((ndx, jj, ndx, l1_minus, 0, l2_minus))
                    elif A[ndx][jj] == 0:
                        d2.append((ndx, jj, ndx, l1_minus, 0, l2_minus))


                    
        for k in range(1, 100):
            m = 2+k
            d1 = deque()
            for i, j, imin, imax, jmin, jmax in d2:
                if A[i][j] == 0: 
                    A[i][j] = m

                    if j > jmin:
                        ndx = j - 1                        
                        if A[i][ndx] == 0:                        
                            d1.append((i, ndx, min_i, l1_minus, 0, ndx))
                        elif A[i][ndx] == 1:
                            return k

                    if j < jmax:
                        ndx = j + 1
                        if A[i][ndx] == 0: 
                            d1.append((i, ndx, min_i, l1_minus, ndx, l2_minus))
                        elif A[i][ndx] == 1:
                            return k


                    if i > imin:
                        ndx = i - 1
                        if A[ndx][j] == 0:
                            d1.append((ndx, j, min_i, ndx, 0, l2_minus))
                        elif A[ndx][j] == 1:
                            return k

                    if i < imax:
                        ndx = i + 1
                        if A[ndx][j] == 0:
                            d1.append((ndx, j, ndx, l1_minus, 0, l2_minus))
                        elif A[ndx][j] == 1:
                            return k
                                             
                  
            d2 = d1

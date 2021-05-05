class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        max_val = -inf
        j = 1
        j_max = 0
        i = 0
        array_len = len(points)
        x1 = points[i][0]
        y1 = points[i][1]

        while j < array_len:
            if j > j_max:
                tmp = (points[j][0] - x1) 
                if tmp <= k:
                    y2 = points[j][1]
                    tmp2 = tmp + y1
                    max_val = max(max_val, tmp2 + y2) 
                    if tmp2 < y2:                    
                        i = j
                        x1 = points[i][0]
                        y1 = points[i][1]
                    j_max = j
                    j = j + 1
                else:
                    i = i + 1
                    j = i + 1
                    x1 = points[i][0]
                    y1 = points[i][1]
            else:
                if (points[j][0] - x1) + y1 < points[j][1]:                    
                    i = j
                    x1 = points[i][0]
                    y1 = points[i][1]
                j = j + 1
                

        return max_val
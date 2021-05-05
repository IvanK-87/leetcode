class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        l = len(points)

        dd = defaultdict(int)
        dd[1] = 0        
        d = defaultdict(int)
        d[1] = 0
        for i in range(l):
            x = points[i][0]
            y = points[i][1]
            dd[x] += 1
            for j in range(i, l):
                dx = points[j][0] - x
                if dx != 0:
                    k = round((points[j][1]-y)/dx, 10)
                    d[(k, i)] += 1
        max_num_new = max(d.values())+1
        max_num = max(dd.values())
        return max(max_num_new, max_num)
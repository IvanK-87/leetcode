class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
      
        def get_iteration(x, y, pos, n):
            dist = 0.
            d = 0.
            a = 0.
            b = 0.
            c = 0.
            for i in range(n):
                xx = pos[i][0]
                yy = pos[i][1]
                tmp = (x - xx)*(x - xx)
                tmp += (y - yy)*(y - yy)
                d = max(0.00000001, sqrt(tmp))
                dist += d
                a += 1./d
                b += xx/d
                c += yy/d
            return(b/a, c/a, dist)
        
        n = len(positions)
        if n == 1:
            return 0
        
        x_sum = 0.
        y_sum = 0.

        for i in range(n):
            x_sum += positions[i][0]
            y_sum += positions[i][1]

        d = d_new = inf
        x = x_sum/n
        y = y_sum/n
        for i in range(1000):
            x_new, y_new, d_new = get_iteration(x, y, positions, n)
            if d - d_new < 0.0000005:
                return d_new
            else:
                x += (x_new - x)*1.8
                y += (y_new - y)*1.8
                d = d_new
            
        return d_new
        
            
        
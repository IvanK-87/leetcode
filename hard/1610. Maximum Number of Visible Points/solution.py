class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        l = len(points)
        
        x0 = location[0]
        y0 = location[1]
        ang = radians(angle)
        full_circle = 2*pi
        
        same_pos = 0
        angles_lst = []
        for i in range(l):
            x1 = points[i][0] - x0
            y1 = points[i][1] - y0
            if x1 == 0 and y1 == 0:
                same_pos += 1
            else:
                a = atan2(y1, x1)
                angles_lst.append(a)

                
        if len(angles_lst) <= 1:
            return l
                
        angles_lst.sort()

        l = len(angles_lst)
        i = j = -l
        max_val = 1

        while True:
            a = angles_lst[i] - full_circle
            j = i + max_val 
            r = l - max_val
            for k in range(r):            
                if (angles_lst[j] - a) % full_circle > ang:
                    break
                j += 1
            else:
                return (l + same_pos)

            max_val = j-i

            a = angles_lst[j] + full_circle
            for k in range(max_val):
                i += 1
                if i >= 0:
                    return (max_val + same_pos)
                elif (a - angles_lst[i]) % full_circle <= ang:
                    break

        return (max_val + same_pos) 
        
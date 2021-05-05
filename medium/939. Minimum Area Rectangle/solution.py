class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        points.sort(key=itemgetter(0, 1))
        l = len(points)

        ndx_list = deque()
        x_dict = {}
        y_dict = {}
        min_area = inf
        d = {}
        min_x_delta = inf
        min_y_delta = inf
        x1 = -inf
        y1 = -inf
        for p in points:
            x = p[0]
            y = p[1]
            x_dict[x] = 1 + x_dict.get(x, 0)
            y_dict[y] = 1 + y_dict.get(y, 0)

        for p in points:
            x2 = p[0]
            y2 = p[1]
            if x_dict[x2] > 1 and y_dict[y2] > 1:
                ndx_list.append((x2, y2))
                if x1 == x2:
                    x = d.get((y1, y2))
                    d[(y1, y2)] = x2
                    if x is not None:                      
                        min_area = min(min_area, (x2 - x)*(y2 - y1))
                else:
                    min_x_delta = min(min_x_delta, x2 - x1)
                    x1 = x2
                y1 = y2
   
           
        l = len(ndx_list)
        min_val = min_area/min_x_delta

        d = {}
        for i in range(l-1):
            x2, y1 = ndx_list.popleft()
            for x, y2 in ndx_list:
                if x2 < x or y2 - y1 >= min_val:
                    break
                else:                    
                    x1 = d.get((y1, y2))
                    d[(y1, y2)] = x2
                    if x1 is not None:
                        new_area = (x2 - x1)*(y2 - y1)
                        if new_area < min_area:
                            min_area = new_area
                            min_val = min_area/min_x_delta
                            min_val2 = min_area/min_y_delta

        if min_area < inf:
            return min_area
        else:
            return 0


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=itemgetter(0))

        last_point = intervals[-1][0]
        prelast_point = last_point
        s_size = 2 

        for i in reversed(range(len(intervals)-1)):
            x = intervals[i][1]
            if x < last_point:
                s_size += 2
                last_point = intervals[i][0]
                prelast_point = last_point
            elif x > prelast_point:
                continue       
            else:
                s_size += 1
                y = intervals[i][0]
                prelast_point = max(y, last_point-1)
                last_point = y
                     
        return s_size
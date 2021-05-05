class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_dist_tmp = x = y = 0
        distance = [0]*(n+1)
        ndx_num = ndx_num_new = 1

        for i, rng in enumerate(ranges):
            if rng > 0:
                x = i+rng
                if x > max_dist_tmp:
                    y = i-rng                   
                    ndx_num_new = 0
                    for j in reversed(range(ndx_num)):
                        if distance[j] < y:
                            ndx_num_new = j+1
                            break

                    if ndx_num_new < ndx_num: 
                        distance[ndx_num_new+1] = x
                        ndx_num = ndx_num_new + 2
                    elif max_dist_tmp < i-100:
                        return -1
                    max_dist_tmp = x

        if distance[ndx_num-1] < n:
            return -1
        elif distance[ndx_num-2] < n:
            return ndx_num-1
        else:
            return ndx_num-2
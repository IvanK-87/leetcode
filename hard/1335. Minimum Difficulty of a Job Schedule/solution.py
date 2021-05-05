class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jobs_len = len(jobDifficulty)
        if jobs_len < d:
            return -1
        elif d == 1:
            return max(jobDifficulty)
        elif d == 2:
            return min(jobDifficulty[0], jobDifficulty[-1]) + max(jobDifficulty)
            
        elif d == jobs_len:
            return sum(jobDifficulty)

        
        max_values = [0.]*(jobs_len+1)
        max_values_2d = [max_values[:] for j in range(jobs_len+1)]
        for i in range(3, jobs_len+1):
            max_values_2d[1][i] = max(jobDifficulty[i-1:i])
            for j in range(2, i+1):
                max_values_2d[j][i] = max(max_values_2d[j-1][i], jobDifficulty[i-j])
                
        difficult_list_prev = [0., 0] + [min(jobDifficulty[0], jobDifficulty[i-1]) + max(jobDifficulty[:i]) \
                               for i in range(2, jobs_len+1)]
        difficult_list_next = [0.]*(jobs_len+1)
        
        for k in range(3, d+1):
            difficult_list_next[k] = sum(jobDifficulty[:k]) 
            for i in range(k+1, jobs_len+1):
                lst_tmp = [0]*(i-k+1)
                for j in range(1, i-k+2):
                    lst_tmp[j-1] = difficult_list_prev[i-j] + max_values_2d[j][i]
                difficult_list_next[i] = min(lst_tmp)
            tmp = difficult_list_next
            difficult_list_next = difficult_list_prev
            difficult_list_prev = tmp
        return difficult_list_prev[jobs_len]
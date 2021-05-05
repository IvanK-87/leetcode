class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) == k:
            return(sum(cardPoints))
        elif len(cardPoints) == k+1:
            return(sum(cardPoints) - min(cardPoints))
        start_sum = sum(cardPoints[:k])
        score_list = [start_sum]*(k+1)
        for i in range(1, (k+1)):
            score_list[i] = score_list[i-1] + cardPoints[-i] - cardPoints[k-i]
        return(max(score_list))
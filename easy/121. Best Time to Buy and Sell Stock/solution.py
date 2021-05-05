class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def get_min_max_profit(prc):
            if len(prc) < 2:
                return(prc[0], prc[0], 0)
            else:
                prices_len_half = len(prc) // 2
                min_1, max_1, profit_1 = get_min_max_profit(prc[:prices_len_half])
                min_2, max_2, profit_2 = get_min_max_profit(prc[prices_len_half:])
                return(min(min_1, min_2), max(max_1, max_2), max(profit_1, profit_2, max_2-min_1))
        min_1, max_1, profit_1 = get_min_max_profit(prices)
            
        return profit_1
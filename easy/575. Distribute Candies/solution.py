class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:           
        candyType_set = set(candyType)
        types_num = len(candyType_set)
        output = int(min(types_num, len(candyType)/2))
        return output
        
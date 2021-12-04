class Solution:
    def maximumSwap(self, num: int) -> int:
        d = None
        num_str = str(num)
        l = len(num_str)
        if l < 2:
            return num
        i1 = l - 1

        for i2 in reversed(range(l-1)):
            if num_str[i2] < num_str[i1]:
                d = (i2, i1)
            elif num_str[i2] > num_str[i1]:
                i1 = i2

        if d is None:
            return num

        i2, i1 = d
        s1, s2 = num_str[i1], num_str[i2]
        num_str = list(num_str)
        num_str[i1], num_str[i2] = s2, s1
        return int(''.join(num_str))
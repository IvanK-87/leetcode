class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 1:
            return len(s)
        def get_max_substring(ss, kk):
            if len(ss) < kk:
                return 0
            min_letter = Counter(ss).most_common()[-1]

            if min_letter[1] >= kk:
                return len(ss)
            substring_list = ss.split(min_letter[0])

            max_len = 0
            for subs in substring_list:
                max_len = max(max_len, get_max_substring(subs, kk))
            return max_len           
            
        return get_max_substring(s, k)
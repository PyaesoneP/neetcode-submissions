class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        s1_char_counts = {}
        s2_char_count_check = {}
        window_length = 0
        is_included = False

        for s in s1:
            s1_char_counts[s] = s1_char_counts.get(s, 0) + 1
        
        while r < len(s2):
            can_grow = s2[r] in s1_char_counts and s2_char_count_check.get(s2[r], 0) < s1_char_counts[s2[r]]
            if can_grow:
                s2_char_count_check[s2[r]] = s2_char_count_check.get(s2[r], 0) + 1
                r += 1
                window_length = r - l
                if window_length == len(s1):
                    is_included = True
                    return is_included
            else:
                if s2[r] not in s1_char_counts:
                    l = r + 1
                    r = r + 1
                    s2_char_count_check.clear()
                else:
                    s2_char_count_check[s2[l]] = s2_char_count_check[s2[l]] - 1
                    l += 1
        return is_included


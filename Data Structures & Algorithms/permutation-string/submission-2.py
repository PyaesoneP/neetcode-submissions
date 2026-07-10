from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l, r = 0, 0
        s1_count = Counter(s1)
        s2_check = Counter()
        
        while r < len(s2):
            can_grow = s2[r] in s1_count and s2_check[s2[r]] < s1_count[s2[r]]

            if can_grow:
                s2_check[s2[r]] += 1
                r += 1
                if r - l == len(s1):
                    return True
            else:
                if s2[r] not in s1_count:
                    l = r = r + 1
                    s2_check.clear()
                else:
                    s2_check[s2[l]] -= 1
                    l += 1

        return False


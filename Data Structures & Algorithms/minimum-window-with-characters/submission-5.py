import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        t_char_counts = {}
        must_grow = {}
        win_char_count = {}
        best_l, best_r = None, None
        current_length, shortest_length = None, math.inf

        for c in t:
            t_char_counts[c] = t_char_counts.get(c, 0) + 1
            must_grow[c] = must_grow.get(c, 0) + 1

        while True:
            if must_grow:
                if r == len(s):
                    break
                if s[r] in t_char_counts:
                    win_char_count[s[r]] = win_char_count.get(s[r], 0) + 1
                if s[r] in must_grow:
                    must_grow[s[r]] -= 1
                    if must_grow[s[r]] == 0:
                        del must_grow[s[r]]
                r += 1
            
            else:
                current_length = r - l
                if current_length < shortest_length:
                    shortest_length = current_length
                    best_l, best_r = l, r

                if s[l] in t_char_counts:
                    win_char_count[s[l]] -= 1
                    if win_char_count[s[l]] < t_char_counts[s[l]]:
                        must_grow[s[l]] = must_grow.get(s[l], 0) + 1
                    l += 1
                else:
                    l += 1
                

        if best_l == None and best_r == None:
            return ""

        return s[best_l:best_r]

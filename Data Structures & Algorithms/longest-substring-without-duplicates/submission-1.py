class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        longest_length = 0
        unique_chars = set()

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        while r < len(s):
            can_grow = s[r] not in unique_chars
            if can_grow:
                unique_chars.add(s[r])
                r += 1
                longest_length = max(r - l, longest_length)
            else:
                unique_chars.remove(s[l])
                l += 1
        return longest_length
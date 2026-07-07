class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        char_count = {}
        max_freq = 0

        for r in range(len(s)):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            max_freq = max(max_freq, char_count[s[r]])

            while (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        longest_consecutive_length = 0

        for num in unique_nums:
            if num + 1 not in unique_nums:
                current_consecutive_length = 1
                current = num
                while current - 1 in unique_nums:
                    current_consecutive_length += 1
                    current = current - 1
                longest_consecutive_length = max(current_consecutive_length, longest_consecutive_length)

        return longest_consecutive_length

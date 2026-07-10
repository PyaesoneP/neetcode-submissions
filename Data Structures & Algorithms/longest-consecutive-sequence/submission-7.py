class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique_nums = set(nums)

        if len(unique_nums) == 0 or len(unique_nums) == 1:
            return len(unique_nums)

        longest_consequtive_length = 1
        current_consequtive_length = 1

        for num in unique_nums:
            if num + 1 not in unique_nums:
                current = num
                while current - 1 in unique_nums:
                    current_consequtive_length += 1
                    current = current - 1
                longest_consequtive_length = max(current_consequtive_length, longest_consequtive_length)
                current_consequtive_length = 1
        return longest_consequtive_length

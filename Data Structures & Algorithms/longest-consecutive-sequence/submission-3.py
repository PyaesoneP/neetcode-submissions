class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        conseq_counts = {}
        largest_conseq_count = 1
        if len(unique) == 1:
            return 1
        if not unique:
            return 0
        for num in unique:
            if num + 1 not in unique:
                start = num
                while start - 1 in unique:
                    conseq_counts[num] = conseq_counts.get(num, 1) + 1
                    start = start - 1
        for conseq_count in conseq_counts.keys():
            if conseq_counts[conseq_count] > largest_conseq_count:
                largest_conseq_count = conseq_counts[conseq_count]

        return largest_conseq_count

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 0:
            return False
        num_set = set(nums)
        return len(nums) != len(num_set)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            second_num = target - nums[i]

            if second_num in nums:
                if i == nums.index(second_num):
                    continue
                if i < nums.index(second_num):
                    return [i, nums.index(second_num)]
                else:
                    return [nums.index(second_num), i]
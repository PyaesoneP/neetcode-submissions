class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] > 0:
                break
        
            l = i + 1
            r = len(nums) - 1

            while l < r:

                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue

                if nums[l] + nums[r] == -nums[i]:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                elif nums[l] + nums[r] < -nums[i]:
                    l += 1
                else:
                    r -= 1
        return result
             
            
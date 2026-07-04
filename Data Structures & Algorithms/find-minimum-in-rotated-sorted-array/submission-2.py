class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 1
        high = len(nums)
        ans = None

        if nums[0] < nums[-1] or len(nums) == 1:
            ans = nums[0]
            return ans

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid-1]:
                ans = nums[mid]
                break
            elif nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1
        return ans
            
        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1

        if nums[0] < nums[-1] or len(nums) == 1:
            return nums[0]

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[-1]:
                low = mid + 1
            else:
                high = mid - 1
        return nums[low]
            
        
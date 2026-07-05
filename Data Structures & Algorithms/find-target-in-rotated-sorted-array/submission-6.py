class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, len(nums) - 1
        start_index, end_index = 0, len(nums) -1
        rotated = True

        if n == 0:
            return -1

        if nums[l] < nums[r]:
            rotated = False
            r = 0

        while rotated:
            while r - l > 1:
                mid = (r + l) // 2
                if nums[mid] > nums[r]:
                    l = mid
                else:
                    r = mid
            rotated = False
        
        if nums[(start_index+r)%len(nums)] >= target or nums[(end_index+r)%len(nums)] < target:
            if nums[(start_index+r)%len(nums)] == target:
                return (start_index+r)%len(nums)
            return -1

        while end_index - start_index > 1:
            mid = (start_index + end_index) // 2
            if nums[(mid+r)%len(nums)] < target:
                start_index = mid
            else:
                end_index = mid
        if nums[(end_index+r)%len(nums)] == target:
            return (end_index+r)%len(nums)
        return -1
        

        
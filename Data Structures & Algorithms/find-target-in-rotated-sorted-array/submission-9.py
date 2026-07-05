class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n - 1
        start_index, end_index = 0, n - 1
        rotated = True
        pivot = None

        if n == 0:
            return -1

        if nums[l] < nums[r]:
            rotated = False
            pivot = 0

        if rotated:
            while r - l > 1:
                mid = (r + l) // 2
                if nums[mid] > nums[r]:
                    l = mid
                else:
                    r = mid
            pivot = r
        
        if nums[(start_index + pivot) % n] >= target or nums[(end_index + pivot) % n] < target:
            if nums[(start_index + pivot) % n] == target:
                return (start_index + pivot) % n
            return -1

        while end_index - start_index > 1:
            mid = (start_index + end_index) // 2
            if nums[(mid + pivot) % n] < target:
                start_index = mid
            else:
                end_index = mid
        if nums[(end_index + pivot) % n] == target:
            return (end_index + pivot) % n
        return -1
        

        
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = math.ceil(sum(piles) / h)
        high = max(piles)
        mid = None
        while low <= high:
            mid = (low + high) // 2
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile / mid)
            if total_hour <= h:
                high = mid - 1
            elif total_hour > h:
                low = mid + 1
        return low
            


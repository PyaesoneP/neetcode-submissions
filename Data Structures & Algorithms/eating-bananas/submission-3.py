import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        low = math.ceil(sum(piles) / h)
        high = largest
        min_eating_speed = None
        while low <= high:
            mid = (low + high) // 2
            min_eating_speed = mid
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile / mid)
            if total_hour <= h:
                high = mid - 1
            elif total_hour > h:
                low = mid + 1
        return min_eating_speed
            


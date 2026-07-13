import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i, point in enumerate(points):
            heapq.heappush(heap, (-math.sqrt(point[0]**2 + point[1]**2), i, point))
            if len(heap) > k:
                heapq.heappop(heap)
            

        return [point[-1] for point in heap]

        
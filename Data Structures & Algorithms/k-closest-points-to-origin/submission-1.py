import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for i, (x, y) in enumerate(points):
            distance_squared = x**2 + y**2
            heapq.heappush(heap, (-distance_squared, i, (x,y)))
            if len(heap) > k:
                heapq.heappop(heap)
            

        return [point for _,_,point in heap]

        
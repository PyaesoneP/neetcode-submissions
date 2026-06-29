import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        heap = [(value, key) for key, value in counter.items()]    

        heapq.heapify(heap)    

        for i in range(len(heap) - k):
            heapq.heappop(heap)

        return [item[1] for item in heap]
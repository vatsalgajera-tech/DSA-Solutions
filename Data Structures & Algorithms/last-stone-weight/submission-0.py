import heapq

class Solution:
    def lastStoneWeight(self, stones):
        # Convert to max heap using negative values
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            y = -heapq.heappop(maxHeap)   # largest
            x = -heapq.heappop(maxHeap)   # second largest

            if y != x:
                heapq.heappush(maxHeap, -(y - x))

        return -maxHeap[0] if maxHeap else 0
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        arr = sorted(count.items(), key=lambda x: x[1], reverse=True)

        return [num for num, freq in arr[:k]]
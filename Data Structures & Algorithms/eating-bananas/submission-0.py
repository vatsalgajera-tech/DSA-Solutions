class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + mid - 1) // mid

            if hours <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
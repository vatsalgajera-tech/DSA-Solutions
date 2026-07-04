class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1

        while l < r:
            # Array is already sorted
            if nums[l] < nums[r]:
                return nums[l]

            mid = (l + r) // 2

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid

        return nums[l]
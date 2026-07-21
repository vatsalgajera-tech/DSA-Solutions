class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset[:])
                return

            # Include current element
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude current element
            dfs(i + 1)

        dfs(0)
        return res
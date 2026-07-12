class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(i):
            if i == len(nums):
                ans.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return ans
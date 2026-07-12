class Solution:
    def combinationSum(self, nums, target):
        res = []

        def dfs(i, cur, total):
            # Found a valid combination
            if total == target:
                res.append(cur[:])
                return

            # Invalid path
            if i >= len(nums) or total > target:
                return

            # Choose current number
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            # Backtrack
            cur.pop()

            # Skip current number
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxDict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in idxDict:
                return [idxDict[complement], i]

            idxDict[num] = i
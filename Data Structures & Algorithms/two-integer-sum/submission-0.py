class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for idx, val in tuple(enumerate(nums)):
            complement = target - val
            if complement in seen:
                return [seen[complement], idx]
            seen[val] = idx

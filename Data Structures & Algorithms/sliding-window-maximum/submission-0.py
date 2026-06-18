class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        maxes = []

        for i in range(n-k+1):
            maxes.append(max(nums[i:i+k]))

        return maxes
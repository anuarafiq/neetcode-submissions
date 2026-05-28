class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            j, k = i+1, n-1
            if i > 0 and nums[i] == nums[i-1]: continue
            while j < k:
                target = -nums[i]
                curr = nums[j] + nums[k]
                if curr == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: j += 1
                    while j < k and nums[k] == nums[k+1]: k -= 1
                elif curr < target: j += 1
                else: k -= 1
        
        return res
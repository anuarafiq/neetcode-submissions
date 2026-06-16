class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        
        minn = 1001
        l, r = 0, n-1

        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            else:
                mid = (l+r) // 2
                if nums[mid] < nums[l]:
                    l = mid
                else:
                    l = mid + 1

            minn = min(minn, nums[mid])

        return minn
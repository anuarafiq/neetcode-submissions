import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prod_left = 1,1,2,8
        nums = 1,2,4,6
        prod_right = 48,24,6,1

        """
        prod_left = [1] + [math.prod(nums[:i]) for i in range(1, len(nums))]
        prod_right = [math.prod(nums[i:]) for i in range(1, len(nums))] + [1]

        return [l*r for l,r in zip(prod_right, prod_left)]

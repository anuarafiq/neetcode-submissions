class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        prod_left = 1,1,2,8
        nums = 1,2,4,6
        prod_right = 48,24,6,1

        """
        ret = [1 for _ in range(len(nums))]
        prod_right = 1

        # prod_left
        for i in range(1, len(nums)):
            ret[i] = nums[i-1] * ret[i-1]

        # prod_right
        for i in range(len(nums)-1, -1, -1):
            ret[i] *= prod_right
            prod_right *= nums[i]

        return ret
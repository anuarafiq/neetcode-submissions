class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        largest = max(nums)
        smallest = min(nums)
        sequence = 1

        while largest >= smallest:
            if largest in hashset and largest - 1 in hashset:
                sequence += 1
            largest -= 1    

        return sequence
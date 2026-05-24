class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hashset = set(nums)
        sequence = 1
        max_sequence = 1

        for num in nums:
            if num-1 not in hashset:
                sequence = 1
            curr = num
            while curr+1 in hashset:
                sequence += 1
                curr += 1
            max_sequence = max(max_sequence, sequence)

        return max_sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        hashset = set(nums)
        largest = max(nums)
        smallest = min(nums)
        sequence = 1
        max_sequence = 1

        while largest >= smallest:
            if largest in hashset and largest - 1 in hashset:
                sequence += 1
            else:
                sequence = 1
            largest -= 1
            max_sequence = max(max_sequence, sequence)


        return max_sequence
from _heapq import heapify, heappop
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = [(-freq, word) for word, freq in Counter(nums).items()]
        heapq.heapify(heap)

        ans = []
        for i in range(k):
            freq, val = heapq.heappop(heap)
            ans.append(val)

        return ans
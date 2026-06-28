class Solution:
    from collections import Counter

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = Counter(nums)
        arr2 = dict(sorted(arr.items(),reverse=True , key=lambda item: item[1]))
        return list(arr2.keys())[:k]

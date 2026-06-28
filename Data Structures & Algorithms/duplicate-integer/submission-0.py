class Solution:
    from collections import Counter

    def hasDuplicate(self, nums: List[int]) -> bool:
        count1 = Counter(nums)
        for j in count1.values():
            if j > 1:
                return True
        return False

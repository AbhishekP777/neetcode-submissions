class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        check = set(nums)
        ans = 0

        for n in check:

            if n - 1 not in check:

                length = 1
                num = n

                while num + 1 in check:
                    length += 1
                    num += 1

                ans = max(ans, length)

        return ans
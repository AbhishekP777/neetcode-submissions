class Solution:
    import heapq
    def longestConsecutive(self, nums: List[int]) -> int:
        
        check = set(nums)
        ans = 0 
        for n in nums :
            max = 0

            # checking if n-1 exists i.e if n is the start of series or not
            if n-1 not in check :
                max += 1
                num = n
                while num+1 in check :
                    max += 1
                    num += 1
            
            if max > ans :
                ans = max 
        
        return ans
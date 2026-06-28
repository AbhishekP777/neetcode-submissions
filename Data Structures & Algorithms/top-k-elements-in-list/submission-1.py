class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        count = Counter(nums)
        bucket = [[] for i in range(n+1)]

        ans=[]
        for i,j in count.items():
            bucket[j].append(i)
        
        for i in range(n,0,-1):
            if k == 0 :
                break
            if bucket[i] :
                for num in bucket[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
            else :
                continue

        
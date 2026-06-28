class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         if (nums[i]+nums[j]) == target:
        #             return [i,j]

        n = len(nums)
        ans=[]
        check = {}
        for i in range(n):
            if target-nums[i] in check :
                ans.append(i)
                ans.append(check[target - nums[i]])
                ans.sort()
                return ans
            check[nums[i]]=i





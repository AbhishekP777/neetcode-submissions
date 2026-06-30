# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:

#         n = len(nums)
#         res = [1] * n

#         prefix = 1
#         for i in range(n):
#             res[i] = prefix
#             prefix *= nums[i]

#         suffix = 1
#         for i in range(n - 1, -1, -1):
#             res[i] *= suffix
#             suffix *= nums[i]

#         return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        for i in range(1,len(nums)):
         left[i]=left[i-1]*nums[i-1]
        right = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        answer=[1]*len(nums)
        for i in range(len(nums)):
            answer[i]=left[i]*right[i]
        return answer
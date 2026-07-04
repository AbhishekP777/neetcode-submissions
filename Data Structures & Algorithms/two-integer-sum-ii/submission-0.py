class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        check = {}
        for idx , val in enumerate(numbers):
            remain = target - val
            if remain in check :
                return [check[remain],idx+1]
            check[val] = idx+1
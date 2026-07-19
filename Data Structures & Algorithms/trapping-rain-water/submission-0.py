class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = len(height)
        area = 0

        leftmax = [0]*l
        rightmax = [0]*l

        max_l = max_r = 0

        for i in range(l):  # i = 0, 1, 2 ....l-1
            j = l-1-i       # j = l-1 , l-2 , l-3 , .... 0

            leftmax[i] = max_l  # max val in left side of any point
            rightmax[j] = max_r # max val in right side of any point

            max_l = max(max_l , height[i])
            max_r = max(max_r , height[j])

        for i in range(l) :
            min_lr = min(leftmax[i] , rightmax[i])
            val = min_lr - height[i]

            if val > 0 :
                area += val
            

        return area
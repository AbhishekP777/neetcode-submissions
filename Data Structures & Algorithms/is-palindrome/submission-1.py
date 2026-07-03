class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        check1 = []
        check2 = []

        left = 0
        right = n-1
        while left < n and right >= 0 :
            if s[left].isalnum() :
                check1.append(s[left].lower())
            if s[right].isalnum() :
                check2.append(s[right].lower())

            left += 1
            right -= 1
        
        if check1 == check2 : 
            return True
        else : return False
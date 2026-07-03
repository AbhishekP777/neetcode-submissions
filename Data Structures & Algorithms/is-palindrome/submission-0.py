class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        check = []
        for i in s :
            if i.isalnum() :
                if i.isalpha():
                    check.append(i.lower())
                else : check.append(i)
        
        if check[:] == check[::-1] :
            return True
        else : 
            return False
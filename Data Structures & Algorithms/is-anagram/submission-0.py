class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = list(t)
        for word in s:
            if word in check :
                check.remove(word)
            else :
                return False
        if check:
            return False
        else :
            return True
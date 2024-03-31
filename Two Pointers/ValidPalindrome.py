class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        ls = list(s)
        for i in ls:
            if i.isalnum():
                new.append(str(i).lower())
        if new[::-1]==new:
            return True
        else:
            return False

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stat = False
        if sorted(list(s)) == sorted(list(t)):
            stat = True
            return stat
        else:
            return stat

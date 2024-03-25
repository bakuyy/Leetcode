class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stat = True
        if sorted(s) != sorted(t):
            stat = False
        return stat
            
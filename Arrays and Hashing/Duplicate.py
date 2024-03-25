class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stat = False
        new = set(nums)
        if len(nums) != len(new):
            stat = True
        return stat
        
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        stat = False
        if len(nums) == len(set(nums)):

            return stat
        else:
            stat = True
            return stat
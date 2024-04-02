class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new = []
        prev = 0
        for i in nums:
            prev += i
            new.append(prev)
        return new
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            n = target-num
            if n in nums and i!=nums.index(n):
                return [i,nums.index(n)]
            
        return []




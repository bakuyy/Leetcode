class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        length = len(nums)
        if length == 1:
            return abs(nums[0] - k)
        
        nums.sort()
        medianIndex = length // 2
        ans = 0

        for i in range(length):
            if i < medianIndex:
                ans += max(0, nums[i] - k)
            elif i == medianIndex:
                ans += abs(k - nums[i])
            else:
                ans += max(0, k - nums[i])

        return ans
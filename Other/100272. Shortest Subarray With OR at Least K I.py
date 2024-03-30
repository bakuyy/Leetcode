class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        subarrays = []
        for n in range(len(nums)):
            for m in range(n+1, len(nums)+1):
                sub = nums[n:m]
                subarrays.append(sub)
        
        special = [0]*len(subarrays)
        minL = float('inf')
        for i in subarrays:
            orVal = 0
            for o in i:
                orVal |= o
            if orVal >= k:
                minL = min(minL, len(i))
        
        if minL == float('inf'):
            return -1
        return minL


                






        
        
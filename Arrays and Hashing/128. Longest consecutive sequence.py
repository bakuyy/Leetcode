class Solution:
    def longestConsecutive(self, nums: List[int]) -> int: 
        nums = list(sorted(set(nums)))
        arr = []
        
        seq = 0
        length = len(nums)
        for i in range(length-1):
                if nums[i+1] - nums[i] ==1:
                    seq += 1
                else:
                    arr.append(seq)
                    seq = 0 
        arr.append(seq)
        ans = max(arr)
        if length == 0:
            return 0
        else:  
            return ans + 1


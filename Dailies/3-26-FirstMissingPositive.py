class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        arr = [False]* (length + 1)

        for num in nums:
            if 0<num<=length:
                arr[num] = True
        
        for i in range(1,length+1):
            if not arr[i]:
                return i
        return length + 1        
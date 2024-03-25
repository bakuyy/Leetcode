class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1]*length 
        right = [1] * length

        for m in range(1,length):
            left[m] = nums[m-1] * left[m-1]

        for n in range(length-2, -1, -1):
            right[n] = right[n+1] * nums[n+1]
        
        answer = [left[i] * right[i] for i in range(length)]
        return answer
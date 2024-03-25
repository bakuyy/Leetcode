class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        left = [1]*length 

        for m in range(1,length):
            left[m] = nums[m-1] * left[m-1]

        right = nums[-1]
        for n in range(length-2, -1, -1):
            left[n] *= right
            right *= nums[n]
            
        return left
            

            
            
                


        


        
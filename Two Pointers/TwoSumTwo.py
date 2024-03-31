class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # store the index 
        # check if the two pointers sum up to the target
        # return our answer
        res = {}
        for i, num in enumerate(numbers):
            n = target-num
            if n in res:
                return [res[n] + 1, i + 1]
            res[num] = i
        return []           


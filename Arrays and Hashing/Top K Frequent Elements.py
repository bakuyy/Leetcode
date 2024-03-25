class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the elements that have the most occurances
        # return the k number of elements
        d = {}

        n = set(nums)
        for i in n:
            d[i] = 0
        
        for i in n:
            count = nums.count(i)
            d[i] = count
        
        l = []
        
        d = sorted(d.items(), key=lambda x: x[1],reverse=True)
        for i in range(k):
            l.append(d[i][0])
        return l
            


            

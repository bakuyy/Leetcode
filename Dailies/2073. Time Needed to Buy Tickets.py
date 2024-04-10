class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        length = len(tickets)
        count = 0
        while tickets[k] != 0:
            for i in range(length):

                if tickets[k] ==0:
                    break
                if tickets[i] ==0:
                    continue
                tickets[i] = tickets[i]-1
                count += 1
        print(tickets)
        return count
        
            
        
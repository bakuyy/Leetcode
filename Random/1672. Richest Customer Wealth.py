class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        totalWealth = []
        for i in accounts:
            wealth = 0
            for n in i:
                wealth += n
            totalWealth.append(wealth)
        return max(totalWealth)

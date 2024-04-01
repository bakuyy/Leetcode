class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        res = []

        for s in strs:
            string = ''.join(sorted(s))
            if string in mp:
                res[mp[string]].append(s)
            else:
                mp[string] = len(res)
                res.append([s])
        return res
    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        n = []
        for i in strs:
            n.append(''.join(sorted(i)))
        unique = set(n)

        for i in unique:
            output[i] = []


        for i in strs:
            string = ''.join(sorted(i))
            if string in list(output):
                output[string].append(''.join(i))


        new = []
        for i in output.keys():
            new.append(output.get(i))
            
        return new


            


        
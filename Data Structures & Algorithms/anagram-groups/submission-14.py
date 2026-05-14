class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        Hash = {}

        for word in strs:
            sortWord = "".join(sorted(word))
            if sortWord not in Hash:
                Hash[sortWord] = [word]
            else:
                Hash[sortWord].append(word)

        return list(Hash.values())
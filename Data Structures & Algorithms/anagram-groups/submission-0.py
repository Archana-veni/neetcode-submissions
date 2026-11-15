class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newdict={}
        for words in strs:
            keys="".join(sorted(words))
            if keys not in newdict:
                newdict[keys]=[]
            newdict[keys].append(words)
        return list(newdict.values())
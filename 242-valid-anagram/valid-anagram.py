class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        elementDict={}

        for letter in s:
            if letter in elementDict:
                elementDict[letter]+=1
            else:
                elementDict[letter]=1

        for letter in t:
            if letter in elementDict and elementDict[letter]>0:
                elementDict[letter]-=1
            else:
                return False

        for letter in s:
            if elementDict[letter]>0:
                return False

        return True
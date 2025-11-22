class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        elementDict={}
        indexCounter=0

        anagramsList=[]

        for element in strs:

            sortedElement= "".join(sorted(element))

            if sortedElement not in elementDict:

                elementDict[sortedElement]=indexCounter

                anagramsList.append([element])
                indexCounter+=1

            else:
                anagramsList[elementDict[sortedElement]].append(element)

        return anagramsList

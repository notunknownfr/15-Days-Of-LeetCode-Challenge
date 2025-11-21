class Solution:
    def lengthOfLongestSubstring(self,s):
        setToReturn=set()

        largest=0

        left=0

        for right in range(len(s)):

            while s[right] in setToReturn:

                setToReturn.remove(s[left])
                left+=1
            
            setToReturn.add(s[right])
            largest=max(largest, right-left+1)

        return largest
        

    
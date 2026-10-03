class Solution:
    def isPalindrome(self, x: int) -> bool:
        newlist=[]
        x=str(x)
        for i in range(len(x)-1,-1,-1):
            newlist.append(x[i])
        

        if "".join(newlist)==x:
            return True

        return False

        

        
                

           
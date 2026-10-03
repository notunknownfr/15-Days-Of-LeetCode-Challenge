class Solution:
    def isPalindrome(self, x: int) -> bool:
        reverse=""
        x=str(x)
        for i in range(len(x)-1,-1,-1):
            reverse+=x[i]
        

        if reverse==x:
            return True

        return False

        

        
                

           
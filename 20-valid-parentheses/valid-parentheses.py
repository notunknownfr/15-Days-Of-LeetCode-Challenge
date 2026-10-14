class Solution:
    def isValid(self, s: str) -> bool:
        
        start=0
        stack=[]
        while start!=len(s):
            if s[start] in ["[","(","{"]:
                stack.append(s[start])
                start+=1

            else:
                if len(stack)==0:
                    return False
                elif s[start]=="]" and stack[-1]=="[":
                    stack.pop()

                elif s[start]==")" and stack[-1]=="(":
                    stack.pop()

                elif s[start]=="}" and stack[-1]=="{":
                    stack.pop()
                else:
                    return False
                
                start+=1
        return len(stack)==0
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        summ=0
        i=len(s)-1
        while i!=-1:
            if i!=0:
                if s[i]=="V" and s[i-1]=="I":
                    summ+=4
                    i-=2
                elif s[i]=="X" and s[i-1]=="I":
                    summ+=9
                    i-=2
                elif s[i]=="L" and s[i-1]=="X":
                    summ+=40
                    i-=2
                elif s[i]=="C" and s[i-1]=="X":
                    summ+=90
                    i-=2
                elif s[i]=="D" and s[i-1]=="C":
                    summ+=400
                    i-=2
                elif s[i]=="M" and s[i-1]=="C":
                    summ+=900
                    i-=2
                else:
                    summ+=roman_dict[s[i]]
                    i-=1
            else:
                summ+=roman_dict[s[i]]

                i-=1

        return summ
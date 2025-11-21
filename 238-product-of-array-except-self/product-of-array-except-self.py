class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newarr=[1]
        newarr2=[1]
        newarr3=[]
        for i in range(1,len(nums)):
            newarr.append(newarr[i-1]* nums[i-1])

        x=0
        for i in range(len(nums)-2,-1,-1):
            newarr2.append(newarr2[x]* nums[i+1])
            x+=1
            
        for x in range(len(newarr)):
            newarr3.append(newarr[x]*newarr2[len(newarr2)-1-x])

        return newarr3
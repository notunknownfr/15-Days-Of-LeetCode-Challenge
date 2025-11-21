class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newarr=[1]
        
        for i in range(1,len(nums)):
            newarr.append(newarr[i-1]* nums[i-1])

        right=1
        for i in range(len(nums)-1,-1,-1):
            newarr[i]=newarr[i]* right
            right*=nums[i]
            
            
       
        return newarr

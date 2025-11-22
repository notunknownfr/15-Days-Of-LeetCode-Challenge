class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
            
        currentSum=0
        maxSum=float('-inf')

        for element in nums:
            currentSum+=element
            maxSum=max(currentSum,maxSum)
            if currentSum<0:
                currentSum=0

        return maxSum
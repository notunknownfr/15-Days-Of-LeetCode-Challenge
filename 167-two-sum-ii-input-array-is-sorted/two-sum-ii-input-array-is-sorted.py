class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower=0
        upper=(len(numbers)-1)

        while upper>=lower and numbers[upper]+numbers[lower]!=target:
            if numbers[lower]+numbers[upper]<target:
                lower+=1
            elif numbers[lower]+numbers[upper]>target:
                upper-=1
        
        if numbers[upper]+numbers[lower]==target:
            return [lower+1,upper+1]
        return None
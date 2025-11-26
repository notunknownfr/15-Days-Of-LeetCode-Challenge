class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lower=0
        upper=(len(numbers)-1)

        while upper!=lower:
            if numbers[lower]+numbers[upper]<target:
                lower+=1
            elif numbers[lower]+numbers[upper]>target:
                upper-=1
            else:
                return [lower+1,upper+1]
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_dict={}

        for num in nums:
            if num in element_dict:
                element_dict[num]+=1

                
            else:
                element_dict[num]=1

            if element_dict[num]>len(nums)/2:
                    return num

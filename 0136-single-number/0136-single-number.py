class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
           if nums[i] in dict:
                dict[nums[i]] += dict[nums[i]]+1
           else:
               dict.update({nums[i] :  1}) 
        for x,y in dict.items():
            if y == 1:
                return x           
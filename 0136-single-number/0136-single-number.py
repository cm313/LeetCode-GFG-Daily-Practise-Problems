class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in range(len(nums)):
            val = dict.setdefault(nums[i],0) + 1
            dict[nums[i]] = val
        for key, val in  dict.items():
            if val == 1:
                return key       

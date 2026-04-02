class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        n =  len(nums)
        for i in range(n):
           count = dict.setdefault(nums[i],0)
           # dict.update({nums[i], count+1})
           dict[nums[i]] = count+1
        for key, value in dict.items():
            if value > n/2:
                return key

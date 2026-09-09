class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        my_dict = {}
        for i in range(len(nums)):
          my_dict[nums[i]] = my_dict.setdefault(nums[i],0) + 1

        for key, val in my_dict.items():
                if val == 1:
                    return key
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for val in nums:
            if nums.count(val) == 1:
                return val
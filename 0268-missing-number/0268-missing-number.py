class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        r_sum = int((n*(n+1))/2)
        c_sum = 0
        for i in nums:
            c_sum += i
        return r_sum - c_sum    
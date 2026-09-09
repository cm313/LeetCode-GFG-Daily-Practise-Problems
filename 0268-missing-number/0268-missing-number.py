class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_total = (n*(n+1))//2
        sum_curr = 0
        for val in nums:
            sum_curr = sum_curr+val
        return sum_total - sum_curr    
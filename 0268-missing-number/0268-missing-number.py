class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        n = len(nums)
        total_sum = int((n*(n+1))/2)
        for i in nums:
            sum += i
        res = total_sum-sum
        return res     
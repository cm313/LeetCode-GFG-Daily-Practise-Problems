class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n+1):
            if i in nums:
                continue
            else:
                return i    
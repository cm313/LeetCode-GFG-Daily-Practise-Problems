class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_val = -100000
        cur_sum = 0
        for i in nums:
            cur_sum += i
            if cur_sum > max_val:
                max_val = cur_sum
            cur_sum = max(cur_sum, 0)  
        return max_val            
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        count_neg = 0
        count_pos = 0
        for i in nums:
            if i > 0:
                count_pos += 1
            if i < 0:
                count_neg += 1    
        return max(count_pos, count_neg)       
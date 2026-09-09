class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        i,j = 0,0
        n = len(nums)
        while(j<n):
            if nums[j] == 1:
                j += 1
            else:
                max_count = max(max_count, j-i)
                i = j+1
                j += 1
        max_count = max(max_count, j-i)        
        return max_count            

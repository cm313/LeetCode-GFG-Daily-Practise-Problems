class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        cur_sum = 0
        count = defaultdict(int)
        l = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            count[nums[r]] += 1
            
            if r-l+1 > k:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    count.pop(nums[l])   
                cur_sum -= nums[l]
                l += 1    

            if len(count) == r-l+1 == k:
                max_sum = max(cur_sum,max_sum)    
        return max_sum        
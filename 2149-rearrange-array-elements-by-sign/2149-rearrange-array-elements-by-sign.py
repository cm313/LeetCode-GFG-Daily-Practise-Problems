class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = []
        pos,neg = 0,1
        for i in range(len(nums)):
            if nums[i] > 0:
                ans.insert(pos,nums[i])
                pos += 2
            if nums[i] < 0:
                ans.insert(neg,nums[i])  
                neg += 2
        return ans          

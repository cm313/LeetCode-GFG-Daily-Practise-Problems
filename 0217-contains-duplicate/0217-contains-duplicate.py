class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        i=0
        j=1
        nums.sort()
        while j < n:
            if nums[i] == nums[j]:
                return  True
            else:
                i+=1
                j+=1    
        return False    

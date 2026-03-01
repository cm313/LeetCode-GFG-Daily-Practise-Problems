class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[slow] == nums[fast]:
                continue
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]    
        return slow+1    
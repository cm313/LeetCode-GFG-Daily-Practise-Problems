class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        c_val = nums.count(val)
        c_nums = len(nums)
        res = c_nums - c_val
        i = 0
        j = n-1
        while(i<j):
            if nums[i] != val:
                i = i+1
            if nums[j] == val:
                j = j-1
            if nums[i] == val and nums[j] != val:
                nums[i] = nums[j]
                i=i+1
                j = j-1 
        return res                      
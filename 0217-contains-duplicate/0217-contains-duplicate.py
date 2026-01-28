class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_len = len(nums)
        this_set = set(nums)
        set_len = len(this_set)
        if(nums_len == set_len):
            return False
        else:
            return True 


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        maj_ele = nums[0]
        votes = 1
        for i in range(1,n):
            if nums[i] == maj_ele:
                votes += 1
            else:
                votes -= 1
            if votes == 0:
                votes += 1
                maj_ele = nums[i]
        return maj_ele           
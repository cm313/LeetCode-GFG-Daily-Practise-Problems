class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        thisDict:dict = {}
        for i in range(len(nums)):
            if nums[i] in thisDict:
                thisDict[nums[i]] = thisDict[nums[i]]+1
            else: 
                thisDict[nums[i]] = 1
        for i,j in thisDict.items():
            if j == 1:
                return i        
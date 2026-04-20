class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        res = []
        for i in range(len(nums)):
            val = dict.get(target-nums[i])
            if val != None:
                res.append(i)
                res.append(val)
            else:
                dict[nums[i]] = i
        return res            
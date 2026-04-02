class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dict = {}
        # n =  len(nums)
        # for i in range(n):
        #    count = dict.setdefault(nums[i],0)
        #    # dict.update({nums[i], count+1})
        #    dict[nums[i]] = count+1
        # for key, value in dict.items():
        #     if value > n/2:
        #         return key
        nums.sort()
        count = 0 
        i, j = 0,0
        n = len(nums)
        if n == 1:
            return nums[0]
        while (j<n-1):
            if nums[j] == nums[j+1]:
                count += 1
                j += 1
            else:
                if count+1 > n/2:
                    return nums[j]
                else:
                    count = 0
                    j = j+1
                    i = j   
        if count+1 > n/2:
            return nums[j]                 
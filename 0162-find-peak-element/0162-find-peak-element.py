class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s,e =0,len(nums)-1
        while s<e:
            mid = s+ (e-s)//2
            if nums[mid]>nums[mid+1]:
                e=mid
            else:
                s=mid+1    
        return s        
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        s,e =0,len(nums)-1
        while s<=e:
            mid = s+ (e-s)//2
            if mid > 0 and nums[mid] < nums[mid-1]:
                e = mid-1
            elif mid < len(nums)-1 and nums[mid] < nums[mid+1]:
                s = mid+1
            else:
                return mid
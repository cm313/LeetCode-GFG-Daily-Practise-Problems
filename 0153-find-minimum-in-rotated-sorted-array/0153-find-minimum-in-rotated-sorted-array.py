class Solution:
    def findMin(self, nums: List[int]) -> int:
         n = len(nums)
         s,e = 0, n-1
         while(s<=e):
            mid = s + (e-s)//2
            if nums[mid] > nums[n-1]:
                s = mid+1
            elif nums[mid]<= nums[n-1]:
                ans = nums[mid]
                e = mid-1
         return ans            

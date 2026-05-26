class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]   

    def binarySearch(self,nums: List[int], target: int, goLeft:bool):    
        n = len(nums)
        s,e = 0, n-1
        i = -1
        while(s<=e):
            mid = s+(e-s)//2
            if nums[mid] > target:
               e = mid-1
            elif nums[mid] < target:
                s = mid+1
            else:
                i = mid
                if goLeft:
                    e = mid-1
                else: 
                    s = mid+1
        return i                
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        s,e = 0, n-1
        ans = -1
        if n == 1:
            return nums[0]
        while(s <= e):
            mid = s + (e-s)//2
            if mid == 0:
                if nums[mid] == nums[mid+1]:
                    s = mid+2
                else:
                    ans = nums[mid]
                    break
            elif mid == n-1:
                if nums[mid] == nums[mid-1]:
                    e = mid-2
                else:
                    ans = nums[mid]  
                    break        
            else:
                if mid%2 == 0:
                    if nums[mid] == nums[mid-1]:
                        e  = mid-2
                    elif nums[mid] == nums[mid+1]:
                        s = mid+2    
                    else:
                        ans = nums[mid]   
                        break
                else:
                    if nums[mid] == nums[mid-1]:
                        s = mid+1
                    elif nums[mid] == nums[mid+1]:
                        e = mid-1 
                    else:
                        ans = nums[mid]  
                        break         
        return ans    

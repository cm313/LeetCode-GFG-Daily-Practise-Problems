class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        k = n-1
        if n == 1 :
            if nums[0] == target :
                return 0
            else:
                return -1    
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                continue
            else:
                k = i
                break;   
        s, e = 0, k
        ans = -1
        while (s<=e):
            mid = s+int((e-s)/2)
            if nums[mid] == target:
                ans = nums.index(nums[mid])
                return ans
            elif nums[mid] < target:
                s = mid+1
            else:
                e = mid-1     
        if ans == -1 and k != n-1:
            s,e = k+1,n-1
            while (s<=e):
                mid = s+int((e-s)/2)
                if nums[mid] == target:
                    ans = nums.index(nums[mid])
                    return ans
                elif nums[mid] < target:
                    s = mid+1
                else:
                    e = mid-1  
        return ans        


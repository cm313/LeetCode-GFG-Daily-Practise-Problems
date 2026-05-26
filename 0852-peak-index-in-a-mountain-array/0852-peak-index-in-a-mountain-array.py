class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n =len(arr)
        s,e = 0, n-1
        while(s<=e):
            mid = s + (e-s)//2
            if mid < n-1 and arr[mid] > arr[mid+1]:
                ans = mid
                e = mid-1
            elif mid <n-1 and arr[mid] < arr[mid+1]:
                s = mid+1
        return ans       
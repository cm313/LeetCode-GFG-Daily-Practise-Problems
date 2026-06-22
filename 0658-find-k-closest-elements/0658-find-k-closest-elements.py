class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        idx = self.binarySearch(arr, x)
        i,j = idx-1, idx
        while(i>=0 or j <n) and (j-i-1)<k:
                if i>=0 and j<n:
                    if abs(arr[i]-x) <= abs(arr[j]-x):
                        i =  i-1
                    else:
                        j += 1 
                elif  i >=0:
                    i -= 1
                elif j < n:
                    j += 1                         
        return  arr[i+1:j] 

    def binarySearch(self, arr:List[int], x:int):
        n = len(arr)
        s,e = 0, n-1
        while(s<=e):
            mid = s + (e-s)//2
            if arr[mid] == x:  
                return mid
            elif arr[mid] > x:
                e = mid-1
            else:
                s = mid+1  
        return  s         
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum = 0
        count = 0
        i,j = 0,0 
        n = len(arr)
        while(j<n):
            if j<k:
                sum += arr[j]
                j += 1
            else:
                if sum/k >= threshold:
                    count += 1  
                sum = sum + arr[j] - arr[i]
                j += 1
                i += 1  
        if sum/k >= threshold:
            count += 1        
        return count;        
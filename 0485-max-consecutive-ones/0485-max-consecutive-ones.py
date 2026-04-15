class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       maxVal, count,i,j = 0,0,0,0
       n = len(nums)
       while(j<n):
         if nums[j]!=0:
            j += 1
         elif nums[j] == 0:
            maxVal = max(maxVal,j-i)
            j+=1
            i=j
       maxVal = max(maxVal, j-i)
       return maxVal       
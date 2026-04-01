class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        final_list = []
        start,end = 0,1
        n = len(nums)
          
        while(end < n):
            if nums[end] == nums[end-1]+1:
                end+=1
            else:
                if start == end-1:
                    final_list.append(f"{nums[start]}")
                else:
                    final_list.append(f"{nums[start]}->{nums[end-1]}")        
                start=end
                end+=1  

        if end == n and start==end-1:
            final_list.append(f"{nums[end-1]}")
        elif end==n and start!=end-1:
            final_list.append(f"{nums[start]}->{nums[end-1]}")        
                  
        return final_list          
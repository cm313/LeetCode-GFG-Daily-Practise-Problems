class Solution:
    def hrsRequired(self, piles: List[int], k: int) -> int:
        n = len(piles)
        i = 0
        hrs = 0
        new_piles = piles.copy()
        for i in range(n):
            hrs += int(piles[i]/k)
            if(piles[i]%k != 0):
                hrs += 1     
        return hrs            



    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k, max_k = 1, 0
        for i in range(len(piles)):
            max_k = max(max_k, piles[i])
        # for i in range(min_k, max_k+1):
        #    hrs = self.hrsRequired(piles, i)
        #    if hrs <= h:
        #         return i    
        s,e = min_k, max_k
        ans = 0
        while(s<=e):
            mid_k = int((s+e)/2)
            if self.hrsRequired(piles, mid_k) > h:
                s = mid_k+1
            else:
                ans = mid_k
                e = mid_k-1
        return ans       
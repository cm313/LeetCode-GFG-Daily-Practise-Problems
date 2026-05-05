class Solution:
    def daysRequired(self, cap:int, weights: List[int]):
        n = len(weights)
        weightsOnShip = 0
        days_taken = 1
        for i in range(n):
            remain_cap = cap - weightsOnShip
            if weights[i] <= remain_cap:
                weightsOnShip += weights[i]
            else:
                days_taken += 1
                weightsOnShip = 0
                weightsOnShip += weights[i]    
        return days_taken

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap,max_cap,ans = -1,0,-1
        for i in range(len(weights)):
            min_cap = max(min_cap, weights[i])
            max_cap =max_cap+weights[i]   
        s = min_cap
        e = max_cap    
        while(s<=e):
            mid_cap = int((s+e)/2)
            days_obt = self.daysRequired(mid_cap, weights)
            if days_obt <= days:
                ans = mid_cap
                e = mid_cap-1
            else:
                s = mid_cap+1   
        return ans        
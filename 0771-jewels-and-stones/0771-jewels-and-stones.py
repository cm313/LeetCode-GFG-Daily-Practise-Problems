class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for c in jewels:
            count = 0
            if c in stones:
                res = res + stones.count(c)
        return res    
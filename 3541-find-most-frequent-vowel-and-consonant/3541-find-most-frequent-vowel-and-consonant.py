class Solution:
    def maxFreqSum(self, s: str) -> int:
        v_count = 0
        c_count = 0
        v_str = "aeiou"

        for i in s:
            if i in v_str:
                v_count = max(v_count, s.count(i))
            else:
                c_count = max(c_count, s.count(i))
        return v_count+c_count            
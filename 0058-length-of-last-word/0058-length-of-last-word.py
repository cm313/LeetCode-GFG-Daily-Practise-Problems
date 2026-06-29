class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis = s.strip().split(" ")
        return len(lis[-1])
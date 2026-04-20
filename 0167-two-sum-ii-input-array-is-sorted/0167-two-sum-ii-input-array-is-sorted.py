class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        arr = []
        for i, n in enumerate(numbers):
            diff = target - n
            val = dict.get(diff)
            if val == None:
                dict[n] = i
            else:
                arr.append(val+1)
                arr.append(i+1)    
        return arr        
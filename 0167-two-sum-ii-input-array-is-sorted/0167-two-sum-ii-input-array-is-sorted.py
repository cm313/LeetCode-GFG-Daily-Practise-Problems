class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       # dict = {}
       # arr = []
        # for i, n in enumerate(numbers):
        #     diff = target - n
        #     val = dict.get(diff)
        #     if val == None:
        #         dict[n] = i
        #     else:
        #         arr.append(val+1)
        #         arr.append(i+1)    
        # return arr
        n = len(numbers) 
        i,j = 0, n-1
        arr =[]
        while(i<j):
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i]+numbers[j] < target:
                i += 1
            else:
                arr.append(i+1)
                arr.append(j+1)
                j -= 1
                i+=1
        return arr        
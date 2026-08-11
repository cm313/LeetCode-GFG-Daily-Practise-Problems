class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """Brute force approach"""
        # max_len = 0 
        # for i in range(len(s)):
        #     max_freq = 0
        #     dic: dict = {}
        #     for j in range(i,len(s)):
        #         if dic.get(s[j]) == None:
        #             dic[s[j]] = 1
        #         else:    
        #             dic[s[j]] = dic.get(s[j])+1
        #         max_freq = max(max_freq, dic[s[j]])
        #         change = (j-i+1) - max_freq
        #         if change <= k:
        #                 max_len = max(max_len, j-i+1)
        #         else:
        #                 break     
        # return max_len            

        i,j = 0,0 
        n = len(s)
        max_len = 0
        map: dict = {}
        max_freq = 0
        while(j<n):
            if map.get(s[j]) == None:
                map[s[j]] = 1
            else:
                map[s[j]] = map.get(s[j])+1
            max_freq = max(max_freq, map.get(s[j]))
            # else:
            #     map[s[i]] = map.get(s[i])-1
            #     max_freq = max(max_freq, map.get(s[i]))
            #     i+=1
            while (j-i+1)-max_freq > k:
                map[s[i]] = map.get(s[i])-1
                #max_freq = 0 
                # for value in map.values():
                #     max_freq = max(max_freq, value)
                i+=1
            change = (j-i+1) - max_freq
            if change <= k:
                max_len = max(max_len, j-i+1)
                j += 1    
        return max_len        
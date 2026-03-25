class Solution:
    def find_intersection(self, numSmall: List[int], numBig: List[int], res: List[int], track):
        for i in numSmall:
            if i in numBig and track.setdefault(i,0) == 0:
                res.append(i)
                track[i] = track.get(i,0) + 1
        return res        

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res:List[int] = []
        track = {}
        if (len(nums1) < len(nums2)):
           res = self.find_intersection(nums1, nums2, res, track)
        else:
           res = self.find_intersection(nums2, nums1, res, track)    
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0 
        mejor = 0
    
        ultima_pos = {}
        for r, i in enumerate(s):
            if i in ultima_pos:
                l = max(l, ultima_pos[i] + 1)
            lon = r - l + 1 
            if lon > mejor:
                mejor = lon
            ultima_pos[i] = r
        return mejor



   



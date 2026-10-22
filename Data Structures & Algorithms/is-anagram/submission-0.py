class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for i in range(len(s)):
            if s[i] in map:
                map[s[i]] = map[s[i]]+1
            else:
                map[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in map:
                map[t[i]] = map[t[i]] -1
            else:
                return False
        
        for val in map.values():
            if val !=0:
                return False
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        count = [0] * 26
        for i in range(len(s)):
            index = ord(s[i]) -97
            count[index] +=1

        for i in range(len(t)):
            index = ord(t[i]) -97
            count[index] -=1

        for val in count:
            if val !=0:
                return False
        
        return True


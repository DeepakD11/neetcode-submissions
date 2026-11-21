class Solution:

    def encode(self, strs: List[str]) -> str:
        s1= ""
        for s in strs:
            s1 += str(len(s))+"#"+s
        return s1

    def decode(self, s: str) -> List[str]:
        i =0
        arr = []
        while i<len(s):
            j= i
            l=0
            while j<len(s):
                if s[j] == "#":
                    l = int(s[i:j])
                    break
                else:
                    j+=1
            arr.append(s[j+1:j+1+l])
            i = j+1+l
        return arr
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        items = {}
        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            if sorted_text not in items:
                items[sorted_text]= [strs[i]]
            else:
                items[sorted_text].append(strs[i])
        
        return list(items.values())
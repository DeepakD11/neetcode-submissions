class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] = map[nums[i]]+1
            else:
                map[nums[i]] = 1
        
        for val in map.values():
            if val != 1:
                return True
        return False
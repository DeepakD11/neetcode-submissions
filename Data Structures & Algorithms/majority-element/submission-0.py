class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        half = len(nums)/2
        map = {}
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1
                if map[nums[i]] > half:
                    return nums[i]
        return -1
        
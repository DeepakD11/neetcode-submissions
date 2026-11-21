class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        map ={}
        for i in range(len(nums)):
            if nums[i] in map:
                map[nums[i]] +=1
            else:
                map[nums[i]] = 1
        sorted_keys = sorted(map, key=map.get, reverse=True)
        cnt = 0
        arr = []
        for i in range(len(sorted_keys)):
            if cnt>=k:
                return arr
            else:
                arr.append(sorted_keys[i])
                cnt+=1
        return arr
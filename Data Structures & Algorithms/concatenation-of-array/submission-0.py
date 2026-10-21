class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(0,len(nums)*2):
            if i<len(nums):
                arr.append(nums[i])
            else:
                arr.append(nums[i-len(nums)])

        return arr
        
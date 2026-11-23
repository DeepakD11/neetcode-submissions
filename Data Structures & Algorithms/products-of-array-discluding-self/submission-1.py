
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        prefixArr = [1] * len(nums)
        suffixArr = [1] * len(nums)

        prod = 1
        for i in range(len(nums)-1):
            prefixArr[i+1] = prod * nums[i]
            prod *= nums[i]

        prod1 = 1
        for i in range(len(nums)-1, 0, -1):
            suffixArr[i-1] = prod1 * nums[i]
            prod1 *= nums[i]

        for i in range(len(nums)):
            prefixArr[i] *= suffixArr[i]

        return prefixArr

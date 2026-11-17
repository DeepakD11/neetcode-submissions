class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        el = nums[0]
        cnt = 1

        for i in range(1,len(nums)):
            if cnt ==0:
                el = nums[i]
                cnt+=1
            elif nums[i] ==el:
                cnt+=1
            else:
                cnt-=1

        return el
class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        self.mergeSort(nums, 0, len(nums)-1)
        return nums
    def mergeSort(self,nums:list[int],l:int,r:int):
        if l==r:
            return
        left = l
        right = r
        m = (l+r)//2
        self.mergeSort(nums,l,m)
        self.mergeSort(nums,m+1,r)
        self.merge(nums,l,m,r)
    
    def merge(self,nums:list[int],left:int,mid:int,right:int):
        arr = []
        a = left
        b = mid+1
        while(a<=mid and b<=right):
            if nums[a] <=nums[b]:
                arr.append(nums[a])
                a+=1
            else:
                arr.append(nums[b])
                b+=1
        
        while(b<=right):
            arr.append(nums[b])
            b+=1
        
        while(a<=mid):
            arr.append(nums[a])
            a+=1

        nums[left:right + 1] = arr



        
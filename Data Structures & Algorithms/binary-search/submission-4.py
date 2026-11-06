class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search - recursive
        return self.bs(0,len(nums)-1, nums,target) 
 
    def bs(self, l, r, nums, target): 
        if l > r:
            return -1
        m = (r + l) // 2 
        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.bs(l,m-1,nums,target)
        return self.bs(m+1,r,nums,target)

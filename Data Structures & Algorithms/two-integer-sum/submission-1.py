class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i,n in enumerate(nums):
            for j,n in enumerate(nums[i+1:], start=i+1):
                if nums[i] + nums[j] == target:
                    return [i,j]

   
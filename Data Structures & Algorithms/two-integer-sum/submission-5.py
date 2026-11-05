class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate(nums):
            partner = target - n
            if partner in seen: 
                return [seen[partner],i]
            seen[n] = i  

        return []
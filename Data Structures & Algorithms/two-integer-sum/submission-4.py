class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,v in enumerate(nums):
            d[v] = i 
    
        for i,n in enumerate(nums):
            partner = target - n 
            if partner in d and d[partner] != i:
                return [i,d[partner]]
        return []
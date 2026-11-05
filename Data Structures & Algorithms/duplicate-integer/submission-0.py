class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        keyset = set()
        for n in nums: 
            if n in keyset:
                return True
            keyset.add(n)
        return False 
        
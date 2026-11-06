class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # hash map approach N O 1 ( hashing will be N)
        # for loop - N  
        # Binary search - divide length in half 

        for i,n in enumerate(nums):
            if n == target:
                return i
        return -1 
            
        
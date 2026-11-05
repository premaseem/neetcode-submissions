class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s: 
            if c.isalnum():
                arr.append(c.lower())
        # reverse and compare 
        rrr = arr[::-1]
        if arr != rrr:
            return False


        return True
        
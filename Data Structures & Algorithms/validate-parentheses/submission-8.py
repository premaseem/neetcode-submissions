class Solution:
    def isValid(self, s: str) -> bool:  
        # straing replacement 
        while "()" in s or "[]" in s or "{}" in s: 
            s = s.replace("()","").replace("[]","").replace("{}","")
        return s == ""



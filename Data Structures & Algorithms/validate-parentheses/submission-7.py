class Solution:
    def isValid(self, s: str) -> bool:  
        d = {}
        d[')'] = '('
        d['}'] = '{'
        d[']'] = '['

        stack = []
        for b in s: 

            if b in d.keys():
                c = stack.pop() if stack else None
                if c == None or d.get(b) != c:
                    return False
            elif b in d.values(): 
                stack.append(b)
        return len(stack) == 0 



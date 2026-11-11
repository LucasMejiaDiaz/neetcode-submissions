class Solution:
    def isValid(self, s: str) -> bool:

        freq= {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for i in s:
            if i in freq:
                if not stack:
                    return False   
                top = stack.pop()
                if freq[i] != top:
                    return False
            else:
                stack.append(i)
        if stack:
            return False 
        else:
            return True            
        
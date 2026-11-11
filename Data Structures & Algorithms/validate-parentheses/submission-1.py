class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for caracter in s:
            if caracter in "({[":
                stack.append(caracter)
            elif caracter in "]})":
                if len(stack) == 0:
                    return False

                if caracter == "]" and stack[-1] == "[":
                    stack.pop()
                elif caracter == "}" and stack[-1] == "{":
                    stack.pop()
                elif caracter == ")" and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        if len(stack) ==0:
            return True
        else:
            return False 




                


        
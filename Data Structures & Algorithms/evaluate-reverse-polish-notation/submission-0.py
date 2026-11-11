class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in tokens:
            if i in ("+","-","*","/"):
                der = stack.pop()
                izq = stack.pop()
                if i == "+":
                    result = izq + der     
                elif i =="-":
                    result = izq - der                  
                elif i == "*":
                    result  = izq * der  
                elif i == "/":
                    result = int(izq / der)
                stack.append(result)   
            else:
                stack.append(int(i))
        output = stack[0]
        return output

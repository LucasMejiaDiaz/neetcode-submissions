class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        coches = sorted(zip(position, speed), reverse=True)
        

        for posicion, velocidad in coches:
            tiempo = (target - posicion) /velocidad
            if stack:
                if tiempo >  stack[-1]:
                    stack.append(tiempo)
            else:

                stack.append(tiempo)
        return len(stack)
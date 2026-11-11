class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        stack = []
        output = [0] * n

        for i in range(n):
            while stack and temperatures[i]  > temperatures[stack[-1]]:

                indice_anterior = stack.pop()
                output[indice_anterior] = i - indice_anterior
            stack.append(i)
        return output



        
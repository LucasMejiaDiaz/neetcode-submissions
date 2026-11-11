class Solution:

    def encode(self, strs: List[str]) -> str:

        resultado = ""
        for i in strs:
            longitud = len(i)
            resultado += str(longitud) + "#" + i
        return resultado

    def decode(self, s: str) -> List[str]:
        x=0
        numero=""
        resultado =[]
        while x <len(s):
            numero="" 
            while s[x] != "#":
                numero += s[x]
                x +=1
                numeros = int(numero)  
            palabra = s[x+1:(x+1)+numeros]
            x = x+1+numeros
            resultado.append(palabra)
        return resultado


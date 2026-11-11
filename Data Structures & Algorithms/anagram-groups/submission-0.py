class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapa = {}
        for palabra in strs:
            conteo = [0] * 26
            for i in palabra:
                conteo[ord(i)- ord('a')]+=1
            tupla = tuple(conteo)
            if tupla in mapa:
                mapa[tupla].append(palabra)
            else:
                mapa[tupla] = [palabra]
        return list(mapa.values())




class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        i=1
        j = max(piles)

        while i < j:
            mid = (i+j) //2
            totalhoras = 0
            for pile in piles:
                totalhoras += ( pile + mid -1 ) // mid
            if totalhoras >h:
                i = mid+1
            else:
                j = mid
        return i




        
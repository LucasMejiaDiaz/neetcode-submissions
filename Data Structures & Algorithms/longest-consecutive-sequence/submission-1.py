class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        count =0

        for n in nums:
            if n -1 not in num:
                c = 0
                while n in num:
                    c += 1
                    n += 1

                if count < c:
                    count = c
        return count

        

        
        
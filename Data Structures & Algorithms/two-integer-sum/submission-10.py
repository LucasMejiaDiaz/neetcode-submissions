class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        freq = {}


        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in freq:
                return [freq[complemento], i]
            else:
                freq[num] = i
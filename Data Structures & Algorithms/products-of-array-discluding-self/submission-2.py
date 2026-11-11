class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [0] * len(nums)
        i=0
        producto1 =1


        while i < len(nums):
            output[i] = producto1
            producto1 = producto1 *nums[i]
            i+=1

        producto2 =1
        x = len(nums) - 1
        while x >=0:
            output[x] = output[x] *producto2
            producto2 = producto2 * nums[x]
            x-= 1
        return output
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        i = 0
        j = i+1
        k = len(nums) -1

        resultado =[]

        while i < len(nums)-2:

            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i+1
            k = len(nums) -1
            
            while j < k:
                suma = nums[i] + nums[j] + nums[k]

                if suma == 0:
                    resultado.append([nums[i],nums[j],nums[k]])
                    k -= 1
                    j += 1 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif suma > 0:
                    k -= 1
                else:
                    j += 1
            i+=1
        return resultado
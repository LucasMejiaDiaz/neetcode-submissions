class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        output = []

        
        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1
        buckets = [[] for i in range(len(nums) + 1)]

        for num,cantidad in freq.items():
            buckets[cantidad].append(num)

        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                output.append(num)

                if len(output) == k:
                    
                    return output
        


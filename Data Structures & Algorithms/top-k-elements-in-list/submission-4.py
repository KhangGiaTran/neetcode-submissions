class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elements = {}
        for i, num in enumerate(nums):
            elements[num] = elements.get(num, 0) + 1
            
        bucket = [[] for i in range(len(nums))]
        for key, value in elements.items():
            bucket[value - 1].append(key)
        
        res = []
        for i in range(len(bucket)):
            reverse = len(bucket) - 1 - i
            if len(bucket[reverse]) != 0:
                res.extend(bucket[reverse])
            if len(res) >= k:
                break
        return res
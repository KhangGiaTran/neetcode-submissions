class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            sub = target - num
            if sub in hashmap and target == num + sub:
                return [hashmap[sub], i]
            hashmap[num] = i

        return []
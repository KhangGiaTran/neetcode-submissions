class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if hashmap.get(num):
                return True
            hashmap[num] = True

        return False
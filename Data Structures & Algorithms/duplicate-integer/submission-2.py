class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        for num in nums:
            if hashmap.get(num) != None:
                return True
            else:
                hashmap[num] = True

        return False
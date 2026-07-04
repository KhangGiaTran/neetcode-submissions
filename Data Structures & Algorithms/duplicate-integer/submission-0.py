class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for num in nums:
            seen = m.get(num)
            if seen:
                return True
            m[num] = True
        return False
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])

            mid = (l + r) // 2

            item = nums[mid]
            res = min(res, item)
            if item >= nums[l]:
                
                l = mid + 1
            else:
                r = mid - 1
        return res

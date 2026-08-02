class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSome = nums[l] + nums[r] + num
                if threeSome > 0:
                    r -= 1
                elif threeSome < 0:
                    l += 1
                else:
                    result.append([nums[l], nums[r], num])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result
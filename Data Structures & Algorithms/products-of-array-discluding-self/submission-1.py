class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                forward[i] = num
                continue
            forward[i] = forward[i - 1] * num

        backward = [1] * len(nums)
        for i in range(len(nums)):
            r = len(nums) - 1 - i
            num = nums[r]
            if i == 0:
                backward[r] = num
                continue
            backward[r] = backward[r + 1] * num

        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = backward[i + 1]
            elif i == len(nums) - 1:
                res[i] = forward[i - 1]
            else:
                res[i] = forward[i - 1] * backward[i + 1]

        return res
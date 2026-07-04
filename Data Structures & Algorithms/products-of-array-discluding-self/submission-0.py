class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        memoFirst = [1] * len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if i > 0:
                memoFirst[i] = memoFirst[i - 1] * num
            else:
                memoFirst[i] = num

        memoSecond = [1] * len(nums)
        for i in range(len(nums)):
            index = len(nums) - 1 - i
            num = nums[index]
            if i > 0:
                memoSecond[index] = memoSecond[index + 1] * num
            else:
                memoSecond[index] = num

        print(memoFirst)
        print(memoSecond)
        result = [1] * len(nums)
        for i in range(len(nums)):
            prevProduct = 1
            nextProduct = 1
            if i > 0:
                prevProduct = memoFirst[i - 1]
            if i < len(nums) - 1:
                nextProduct = memoSecond[i + 1]
            print("item", nums[i])
            print('prevProduct', prevProduct)
            print('nextProduct', nextProduct)
            result[i] = prevProduct * nextProduct

        return result
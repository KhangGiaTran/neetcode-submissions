class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            num = nums[i]
            ans = hashmap.get(target - num)
            if ans != None:
                if ans < i:
                    return [ans, i]
                else:
                    return [i, ans]
            else:
                hashmap[num] = i

        return []
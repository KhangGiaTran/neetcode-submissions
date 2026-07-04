class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i in range(len(nums)):
            num = nums[i]
            item = hashmap.get(num)
            if item != None:
                if i < item:
                    return [i, item]
                else:
                    return [item, i]
            else:
                hashmap[target - num] = i
        return []
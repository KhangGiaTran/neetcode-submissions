public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> seen = [];
        for (int i = 0; i < nums.Length; i++)
        {
            seen[target - nums[i]] = i;
        }

        for (int i = 0; i < nums.Length; i++)
        {
            if (seen.TryGetValue(nums[i], out int c))
            {
                if (i == c) {
                    continue;
                }
                if (i > c)
                {
                    return [c, i];
                } else
                {
                    return [i, c];
                }
            }
        }
        return [-1, -1];
    }
}

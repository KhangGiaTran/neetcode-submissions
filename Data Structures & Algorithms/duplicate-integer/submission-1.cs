public class Solution {
    public bool hasDuplicate(int[] nums) {
        Dictionary<int, bool> seen = new ();

        foreach (int num in nums)
        {
            bool a;
            if (seen.TryGetValue(num, out a))
            {
                return true;
            }
            seen[num] = true;
        }

        return false;
    }
}
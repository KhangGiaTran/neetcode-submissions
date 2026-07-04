public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
        {
            return false;
        }

        Dictionary<char, int> seen = [];

        foreach (char c in s)
        {
            if (seen.TryGetValue(c, out int count))
            {
                seen[c] = seen[c] + 1;
            } else
            {
                seen[c] = 1;
            }
        }
        foreach (char c in t)
        {
            if (seen.TryGetValue(c, out int count))
            {
                if (seen[c] == 0)
                {
                    return false;
                }

                seen[c] = seen[c] - 1;
            } else
            {
                return false;
            }
        }

        foreach (var kvp in seen)
        {
            if (kvp.Value != 0)
            {
                return false;
            }
        }
        
        return true;
    }
}
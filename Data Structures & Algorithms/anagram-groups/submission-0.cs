public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        Dictionary<string, List<string>> seen = [];

        foreach (var str in strs)
        {
            int[] arr = new int[26];

            foreach (char c in str)
            {
                arr[c - 'a']++;
            }

            string key = string.Join(",", arr);


            if (!seen.ContainsKey(key)) {
                seen[key] = [];
            }
            seen[key].Add(str);
        }

        List<List<string>> result = [];

        foreach (var kvp in seen)
        {
            result.Add(kvp.Value);
        }

        return result;
    }
}

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l = 0
        res = 0

        for char in s:
            if char in unique:
                while char in unique:
                    unique.remove(s[l])
                    l += 1
            unique.add(char)
            res = max(len(unique), res)

        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        found = set() 
        for i, char in enumerate(s):
            while char in found:
                found.remove(s[l])
                l += 1
            found.add(char)
            longest = max(longest, i - l + 1)

        return longest
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        window = set()
        for i, char in enumerate(s):
            while char in window:
                window.remove(s[l])
                l += 1

            window_size = i - l + 1
            window.add(char)
            longest = max(longest, window_size)
        return longest
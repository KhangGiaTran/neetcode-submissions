class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "": return 0
        longest = 1
        l = 0
        window = set()
        for i, char in enumerate(s):
            if i == 0:
                window.add(char)
                continue
            
            window_size = i - l + 1
            if char not in window:
                # unique
                window.add(char)
                longest = max(longest, window_size)
            else:
                while char in window:
                    if s[l] in window:
                        window.remove(s[l])
                    l += 1
                window.add(char)
        return longest
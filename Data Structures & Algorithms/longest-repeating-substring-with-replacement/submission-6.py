class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        longest = 0
        max_freq = 0

        for i, char in enumerate(s):
            window[char] = 1 + window.get(char, 0)

            max_freq = max(max_freq, window[char])

            window_size = i - l + 1

            # if replacements needed exceed k, shrink from left by 1
            if (window_size - max_freq) > k:
                window[s[l]] -= 1
                l += 1
            longest = max(i - l + 1, longest)

        return longest
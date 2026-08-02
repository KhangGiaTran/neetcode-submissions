class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        occurences = {}

        def valid(window: int) -> bool:
            majority = max(occurences.values())
            return window - majority <= k

        l = 0
        max_len = 0
        for r, char in enumerate(s):
            occurences[char] = occurences.get(char, 0) + 1
            if valid(r - l + 1):
                max_len = max(max_len, r - l + 1)
            else:
                while not valid(r - l + 1):
                    occurences[s[l]] -= 1
                    l += 1
        
        return max_len
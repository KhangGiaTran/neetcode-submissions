class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = 0
        longest = 0

        def eval(self) -> bool:
            # find majority & check if minority can be turned into majority
            biggest = 0
            max_key = max(window, key=window.get)
            total = sum(window.values())
            print('eval', max_key, window, total, window[max_key] + k >= total)
            return window[max_key] + k >= total

        for i, char in enumerate(s):
            window[char] = 1 + window.get(char, 0)

            if not eval(self):
                while not eval(self):
                    window[s[l]] -= 1
                    l += 1
            else:
                longest = max(i - l + 1, longest)
                print('logest', longest)
                print(char, l)

        return longest
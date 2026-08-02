class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        need, have = {}, {}
       

        l = 0
        res = [-1, -1]
        shortest = float("infinity")
        for char in t:
            need[char] = need.get(char, 0) + 1
        
        needCount = len(need)
        haveCount = 0
        
        for i, char in enumerate(s):
            if char in need:
                have[char] = have.get(char, 0) + 1

                if have[char] == need[char]:
                    haveCount += 1

                while haveCount == needCount:
                    if (i - l + 1) < shortest:
                        shortest = i - l + 1
                        res = [l, i + 1]

                    c = s[l]
                    if c in need:
                        if have[c] == need[c]:
                            haveCount -= 1
                        have[c] -= 1
                    l += 1


        return s[res[0]:res[1]] if shortest != float("infinity") else ""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, have = {}, {}

        for char in s1:
            need[char] = need.get(char, 0) + 1

        l = 0
        needCount, haveCount = len(need), 0
        for i, char in enumerate(s2):
            # print('window', s2[l:i + 1])
            if char in need:
                have[char] = have.get(char, 0) + 1
                if need[char] == have[char]:
                    haveCount += 1

                # print(needCount, haveCount)
                if needCount == haveCount:
                    return True
                
            if i >= len(s1) - 1:
                c = s2[l]
                if c in need:
                    if have[c] == need[c]:
                        haveCount -= 1
                    have[c] -= 1
                l += 1

        return False
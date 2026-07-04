class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        hashmap = {}
        for char in s:
            item = hashmap.get(char)
            if item != None:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in t:
            item = hashmap.get(char)
            if item != None:
                hashmap[char] -= 1
            else:
                return False

        for value in hashmap.values():
            if value % 2 != 0:
                return False

        return True
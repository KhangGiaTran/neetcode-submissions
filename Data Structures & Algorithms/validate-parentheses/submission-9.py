class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashmap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                if len(stack) == 0 or stack.pop() != hashmap[char]:
                    return False
        if len(stack) > 0:
            return False
        return True
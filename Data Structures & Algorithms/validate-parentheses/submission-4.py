class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.insert(0, ')')
            elif char == '{':
                stack.insert(0, '}')
            elif char == '[':
                stack.insert(0, ']')
            elif char == ')' or char == '}' or char == ']':
                try:
                    item = stack.pop(0)
                    if item != char:
                        return False
                except:
                    return False
            else:
                continue
        if len(stack) > 0:
            return False
        return True

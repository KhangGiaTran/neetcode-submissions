class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            elif char == ')' or char == '}' or char == ']':
                try:
                    item = stack.pop()
                    if item != char:
                        return False
                except:
                    return False
            else:
                continue
        if len(stack) > 0:
            return False
        return True

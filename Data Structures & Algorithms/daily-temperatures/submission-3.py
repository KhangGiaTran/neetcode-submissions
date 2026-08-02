class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack or temp <= temperatures[stack[-1]]:
                pass
            else:
                while stack:
                    index = stack[-1]
                    if temperatures[index] >= temp:
                        break
                    stack.pop()
                    ans[index] = i - index
            print(stack, temp)
            stack.append(i)
        return ans

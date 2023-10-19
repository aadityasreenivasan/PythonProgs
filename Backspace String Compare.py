class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def ans(s):
            stack = []
            for i in s:
                if i == '#' and stack:
                    stack.pop()
                elif i!='#':
                    stack.append(i)
            return stack
        return ans(s) == ans(t) 
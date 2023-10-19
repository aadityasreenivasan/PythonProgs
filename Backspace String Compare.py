class Solution:
    """
    Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

    Note that after backspacing an empty text, the text will continue empty.

    """
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
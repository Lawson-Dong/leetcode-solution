class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for char in s:
            if char in pairs:
                if not stack or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(char)
        if not stack:
            return True
        else:
            return False

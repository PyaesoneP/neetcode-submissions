class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for st in s:
            if st in ['(', '{', '[']:
                stack.append(st)
            else:
                if not stack:
                    return False
                closing_bk = ord(stack.pop())
                if ord(st) - closing_bk <=0 or ord(st) - closing_bk > 5:
                    return False
        return len(stack) == 0
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses_dict ={
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        for p in s:
            if p in parentheses_dict:
                stack.append(p)
            else:
                if not stack:
                    return False
                if p != parentheses_dict[stack.pop()]:
                    return False
        return len(stack) == 0
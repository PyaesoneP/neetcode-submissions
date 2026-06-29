class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for st in s:
            if st == '(':
                stack.append(')')
            elif st == '{':
                stack.append('}')
            elif st == '[':
                stack.append(']')
            else:
                if not stack:
                    return False
                if st != stack.pop():
                    return False
        
        return len(stack) == 0
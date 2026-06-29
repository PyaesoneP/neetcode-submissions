import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.split(r'\W+', s.lower())
        s = "".join(s)
        first_pointer = 0
        second_pointer = len(s)-1
        while (first_pointer <= second_pointer):
            if not s[first_pointer].isalnum():
                    first_pointer + 1
            if not s[second_pointer].isalnum():
                second_pointer -= 1
            if s[first_pointer] != s[second_pointer]:
                return False
            first_pointer += 1
            second_pointer -= 1

        return True
        
            


        
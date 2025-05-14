class Solution:
    def isPalindrome(self, s: str) -> bool:
        f = ''.join(char.lower() for char in s if char.isalnum())
        right = len(f) - 1

        for char in f:
            print(char, " -> ", f[right])
            if char != f[right]:
                return False
            right -= 1
        return True
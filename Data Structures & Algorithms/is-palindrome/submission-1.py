class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanText = ''.join(char.lower() for char in s if char.isalnum())
        left = 0
        right = len(cleanText) - 1
        if len(cleanText) < 2:
            return True
        while (left < right):
            if (cleanText[left] != cleanText[right]):
                return False
            left += 1
            right -= 1
        return True
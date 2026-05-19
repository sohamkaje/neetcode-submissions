class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visitedLetters = set()
        maxL = 0

        for r in range(len(s)):
            while s[r] in visitedLetters:
                visitedLetters.remove(s[left])
                left += 1
            visitedLetters.add(s[r])
            maxL = max(maxL, r - left + 1)
        return maxL
        
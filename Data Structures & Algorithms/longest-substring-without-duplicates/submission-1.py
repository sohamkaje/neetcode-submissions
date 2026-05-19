class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeats = set()
        left = 0
        length = 0

        for right in range(len(s)):
            while s[right] in repeats:
                repeats.remove(s[left])
                left += 1
            repeats.add(s[right])
            length = max(length, right - left + 1)
        
        return length
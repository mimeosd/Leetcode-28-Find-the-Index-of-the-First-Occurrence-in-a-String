class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1

haystack = "sadbutsad"
needle = "sad"

s1 = Solution
print(s1.strStr(s1, haystack=haystack, needle=needle))
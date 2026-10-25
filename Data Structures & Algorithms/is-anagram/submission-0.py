class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        if len(s) != len(t): return False

        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1
        for ch2 in t:
            count_t[ch2] = count_t.get(ch2, 0) + 1
        if count_s == count_t:
            return True
        return False
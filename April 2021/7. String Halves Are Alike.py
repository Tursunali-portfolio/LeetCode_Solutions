class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        m = len(s)//2
        t = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}
        cnt1 = sum((1 for i in s[:m] if i in t))
        cnt2 = sum((1 for i in s[m:] if i in t))
        return cnt1 == cnt2

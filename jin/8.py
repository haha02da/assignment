class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        res = []
        need = [0]*26
        window = [0]*26

        for ch in p:
            need[ord(ch) - ord('a')] += 1

        m = len(p)

        for i in range(m):
            window[ord(s[i])-ord('a')] += 1

        if need == window:
            res.append(0)

        for i in range(m,len(s)):
            window[ord(s[i]) - ord('a')] += 1
            window[ord(s[i-m]) - ord('a')] -= 1

            if window == need:
                res.append(i-m+1)
        return res
        
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        indicies = []
        for i in range(len(s)):
            if s[i] in p:
                if sorted(list(s[i:i+len(p)])) == sorted(list(p)):
                    indicies.append(i)

        return indicies

sol = Solution()

s = "cbaebabacd"
p = "abc"
print(f"Testcase - 1\ns: {s}\np: {p}")
print(f'Answer: {sol.findAnagrams(s,p)}')

s = "abab"
p = "ab"
print(f"\n\nTestcase - 2\ns: {s}\np: {p}")
print(f'Answer: {sol.findAnagrams(s,p)}')
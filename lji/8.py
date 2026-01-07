def findAnagrams(s: str, p: str) -> list[int]:
    length = len(p)
    index = []
    for i in range(0, len(s) - len(p) + 1):
        if sorted(s[i:i+length]) == sorted(p):
            index.append(i)
    print(index)
    return index


findAnagrams("cbaebabacd", "abc")
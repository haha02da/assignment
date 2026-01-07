class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        len_s = len(s)
        len_p = len(p)
        sorted_p = sorted(p)
        diff_len = len_s - len_p

        if diff_len >= 0:
            result = []
            for i in range(diff_len + 1):
                if sorted(s[i:i+len_p]) == sorted_p:
                    result.append(i)
            return result                
        else:
            return []
        
        
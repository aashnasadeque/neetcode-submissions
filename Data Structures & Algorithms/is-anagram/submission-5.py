from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 1. length check
        # 2 count letters of s
        # 3. count letters of t
        # 4. compare

        if len(s) != len(t):
            return False
        
        countS, countT = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            countS[s[i]] += 1 
            countT[t[i]] += 1
            
        if countS == countT:
            return True

        return False





# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
    
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
    
        return i == len(s)

if __name__ == "__main__":
    sol = Solution()
    s = "abc"
    t = "ahbgdc"
    result = sol.isSubsequence(s, t)
    print(result)
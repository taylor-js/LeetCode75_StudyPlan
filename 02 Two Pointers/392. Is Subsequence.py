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
    # Example 1
    s1 = "abc"
    t1 = "ahbgdc"
    is1 = sol.isSubsequence(s1, t1)
    print(is1)
    # Example 2
    s2 = "axc"
    t2 = "ahbgdc"
    is2 = sol.isSubsequence(s2, t2)
    print(is2)
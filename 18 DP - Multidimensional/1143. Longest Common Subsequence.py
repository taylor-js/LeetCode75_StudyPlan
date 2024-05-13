# https://leetcode.com/problems/longest-common-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Length of both input strings
        m, n = len(text1), len(text2)

        # Create a 2D array to store lengths of longest common subsequence.
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Build the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # dp[m][n] contains the length of LCS for text1[0..m-1], text2[0..n-1]
        return dp[m][n]

if __name__ == "__main__":
    s = Solution()
    lcs1 = s.longestCommonSubsequence("abcde", "ace")
    print(lcs1) # Output: 3
    lcs2 = s.longestCommonSubsequence("abc", "abc")
    print(lcs1) # Output: 3
    lcs3 = s.longestCommonSubsequence("abc", "def")
    print(lcs1) # Output: 0

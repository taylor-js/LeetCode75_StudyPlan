# https://leetcode.com/problems/edit-distance/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        # Create a DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base cases
        for i in range(m + 1):
            dp[i][0] = i  # Cost of deleting all characters from word1 to match empty word2
        for j in range(n + 1):
            dp[0][j] = j  # Cost of inserting all characters of word2 to match empty word1
        
        # Fill the dp table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # Characters match, no operation needed
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,  # Deletion
                        dp[i][j - 1] + 1,  # Insertion
                        dp[i - 1][j - 1] + 1  # Replacement
                    )
        
        return dp[m][n]

if __name__ == "__main__":
    s = Solution()
    # Example 1
    md1 = s.minDistance("horse", "ros")
    print(md1)  # Output: 3
    md2 = s.minDistance("intention", "execution")
    print(md2)  # Output: 5

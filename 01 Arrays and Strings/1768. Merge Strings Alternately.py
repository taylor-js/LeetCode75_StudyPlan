# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        i = j = 0
        result = []

        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        result.extend(word1[i:])
        result.extend(word2[j:])

        return ''.join(result)

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    word1 = "abc"
    word2 = "pqr"
    ma1 = sol.mergeAlternately(word1, word2)
    print(ma1)
    # Example 2
    word3 = "ab"
    word4 = "pqrs"
    ma2 = sol.mergeAlternately(word3, word4)
    print(ma2)
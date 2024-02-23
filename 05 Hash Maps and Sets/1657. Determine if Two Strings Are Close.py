# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        n1 = Counter([v for v in c1.values()])
        n2 = Counter([v for v in c2.values()])
        return c1 == c2 or (n1 == n2 and set(word1) == set(word2))
    
if __name__ == "__main__":
    # Input: word1 = "abc", word2 = "bca"
    sol = Solution()
    output_1 = sol.closeStrings("abc", "bca")
    print(output_1)
    # Output: True

    # Input: word1 = "a", word2 = "aa"
    output_2 = sol.closeStrings("a", "aa")
    print(output_2)
    # Output: False

    # Input: word1 = "cabbba", word2 = "abbccc"
    output_3 = sol.closeStrings("cabbba", "abbccc")
    print(output_3)
    # Output: True

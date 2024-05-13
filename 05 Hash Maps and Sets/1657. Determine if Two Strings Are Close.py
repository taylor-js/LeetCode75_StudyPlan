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
    s = Solution()
    # Example 1
    word1 = "abc"
    word2 = "bca"
    cs1 = s.closeStrings(word1, word2)
    print(cs1)
    # Example 2
    word3 = "a"
    word4 = "aa"
    cs2 = s.closeStrings(word3, word4)
    print(cs2)
    # Example 3
    word5 = "cabbba"
    word6 = "abbccc"
    cs3 = s.closeStrings(word5, word6)
    print(cs3)
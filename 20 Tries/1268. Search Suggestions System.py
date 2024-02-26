# https://leetcode.com/problems/search-suggestions-system/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        l, r = 0, len(products) - 1
        result = []

        for i in range(len(searchWord)):
            search = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != search):
                l += 1
            while l <= r and (len(products[r]) <= i or products[r][i] != search):
                r -= 1

            words_left = r - l + 1
            if words_left >= 3:
                result.append([products[l], products[l + 1], products[l + 2]])
            elif words_left == 2:
                result.append([products[l], products[l + 1]])
            elif words_left == 1:
                result.append([products[l]])
            else:
                result.append([])

        return result
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    products1 = ["mobile","mouse","moneypot","monitor","mousepad"]
    searchWord1 = "mouse"
    sp1 = sol.suggestedProducts(products1, searchWord1)
    print(sp1)
    # Example 2
    products2 = ["havana"]
    searchWord2 = "havana"
    sp2 = sol.suggestedProducts(products2, searchWord2)
    print(sp2)
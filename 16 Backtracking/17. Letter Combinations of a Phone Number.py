# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(index, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            possible_letters = phone_map[digits[index]]
            for letter in possible_letters:
                path.append(letter)  # Add the letter to the current path
                backtrack(index + 1, path)  # Move to the next digit
                path.pop()  # Backtrack
        
        combinations = []
        backtrack(0, [])
        
        return combinations

if __name__ == "__main__":
    s = Solution()
    lc1 = s.letterCombinations("23")
    print(lc1)
    lc2 = s.letterCombinations("")
    print(lc2)
    lc3 = s.letterCombinations("2")
    print(lc3)
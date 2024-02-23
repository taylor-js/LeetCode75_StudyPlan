# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        reversed_words = words[::-1]
        reversed_s = ' '.join(reversed_words)

        return reversed_s
    
if __name__ == "__main__":
    sol = Solution()
    s = "  the sky  is blue  "
    result = sol.reverseWords(s)
    print(result)

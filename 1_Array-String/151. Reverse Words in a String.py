class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split()
        reversed_words = words[::-1]
        reversed_s = ' '.join(reversed_words)

        return reversed_s
    
# Example usage:
sol = Solution()
s = "  the sky  is blue  "
result = sol.reverseWords(s)
print(result)  # Output: "blue is sky the"

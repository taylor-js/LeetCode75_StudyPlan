# https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = "aeiouAEIOU"
        s = list(s)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] not in vowels:
                left += 1
                continue
            if s[right] not in vowels:
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        return ''.join(s)

if __name__ == "__main__":
    sol = Solution()
    s = "hello"
    result = sol.reverseVowels(s)
    print(result)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        left, count, result = 0, 0, 0
        for right in range(len(s)):
            count += 1 if s[right] in vowels else 0
            if right - left + 1 > k:
                count -=1 if s[left] in vowels else 0
                left += 1
            result = max(result, count)
        return result
    
if __name__ == "__main__":
    sol = Solution()
    s = "abciiidef"
    k = 3
    result = sol.maxVowels(s, k)
    print(result)
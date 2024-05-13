# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_length = gcd(len(str1), len(str2))

        return str1[:gcd_length]

if __name__ == "__main__":
    s = Solution()
    # Example 1
    str1 = "ABCABC"
    str2 = "ABC"
    gcdos1 = s.gcdOfStrings(str1, str2)
    print(gcdos1)
    # Example 2
    str3 = "ABABAB"
    str4 = "ABAB"
    gcdos2 = s.gcdOfStrings(str3, str4)
    print(gcdos2)
    # Example 3
    str5 = "LEET"
    str6 = "CODE"
    gcdos3 = s.gcdOfStrings(str5, str6)
    print(gcdos3)

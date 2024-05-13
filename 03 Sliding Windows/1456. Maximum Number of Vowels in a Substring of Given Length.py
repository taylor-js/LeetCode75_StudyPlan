# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    # Imagine this class is like a detective that solves a vowel mystery.

    def maxVowels(self, s: str, k: int) -> int:
        # This method is the detective's investigation strategy.
        # It takes a string 's' (a sequence of letters) and an integer 'k' (size of a window),
        # and it tells us how many vowels are in the largest group of letters within any window of size 'k'.

        # Initialize 'result' to 0, which is like the detective's notebook to record the maximum number of vowels.
        result = 0

        # Initialize 'max_vowels' to 0, which is like the detective's current count of vowels in the window.
        max_vowels = 0

        # Define the vowels that the detective is interested in.
        vowels = 'aeiou'

        # The detective uses a special technique, a for loop, to move through the sequence of letters.
        # 'i' is like the detective's position in the sequence, and 'char' is the letter at that position.
        for i, char in enumerate(s):
            # The detective checks if the current letter is a vowel.
            if char in vowels:
                # If yes, the detective increments the count of vowels in the window.
                max_vowels += 1

            # The detective checks if the window has reached its maximum size 'k'.
            # Also, the detective checks if the letter leaving the window was a vowel.
            if i >= k and s[i - k] in vowels:
                # If yes, the detective decrements the count of vowels as that vowel is no longer in the window.
                max_vowels -= 1

            # The detective updates the notebook with the maximum number of vowels seen so far.
            result = max(result, max_vowels)

        # Finally, the detective reports the maximum count of vowels found in any window of size 'k'.
        return result

if __name__ == "__main__":
    s = Solution()
    # Example 1
    s1 = "abciiidef"
    k1 = 3
    mv1 = s.maxVowels(s1, k1)
    print(mv1)
    # Example 2
    s2 = "aeiou"
    k2 = 2
    mv2 = s.maxVowels(s2, k2)
    print(mv2)
    # Example 3
    s3 = "leetcode"
    k3 = 3
    mv3 = s.maxVowels(s3, k3)
    print(mv3)
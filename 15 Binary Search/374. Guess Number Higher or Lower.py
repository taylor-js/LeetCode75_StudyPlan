# https://leetcode.com/problems/guess-number-higher-or-lower/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def guess(self, num: int, pick: int) -> int:
        # This function takes two arguments: num (your guess) and pick (the number to be guessed)
        if num == pick:
            return 0
        elif num < pick:
            return 1
        else:
            return -1

    def guessNumber(self, n: int, pick: int) -> int:
        left = 1
        right = n
        
        while left <= right:
            mid = left + (right - left) // 2
            result = self.guess(mid, pick)
            
            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1  # If the number is not found within the given range

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    n1 = 10
    pick1 = 6
    gn1 = sol.guessNumber(n1, pick1)
    print(gn1)
    # Example 2
    n2 = 1
    pick2 = 1
    gn2 = sol.guessNumber(n2, pick2)
    print(gn2)
    # Example 3
    n3 = 2
    pick3 = 1
    gn3 = sol.guessNumber(n3, pick3)
    print(gn3)
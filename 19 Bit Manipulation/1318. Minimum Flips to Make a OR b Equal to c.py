# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        for i in range(32):  # Since the maximum number for a, b, or c is < 2**30
            # Extract the i-th bit of a, b, and c
            bit_a = (a >> i) & 1
            bit_b = (b >> i) & 1
            bit_c = (c >> i) & 1
            
            if bit_c == 0:
                # Both bit_a and bit_b should be 0
                if bit_a == 1 and bit_b == 1:
                    flips += 2  # Flip both a and b from 1 to 0
                elif bit_a == 1 or bit_b == 1:
                    flips += 1  # Flip either a or b from 1 to 0
            else:
                # bit_c is 1, so at least one of bit_a or bit_b should be 1
                if bit_a == 0 and bit_b == 0:
                    flips += 1  # Flip either a or b from 0 to 1

        return flips
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    mf1 = s.minFlips(2, 6, 5)
    print(mf1)
    # Example 2
    mf2 = s.minFlips(4, 2, 7)
    print(mf2)
    # Example 3
    mf3 = s.minFlips(1, 2, 3)
    print(mf3)
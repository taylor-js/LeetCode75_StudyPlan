# https://leetcode.com/problems/n-th-tribonacci-number/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def tribonacci(n):
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1

        t0, t1, t2 = 0, 1, 1
        for i in range(3, n + 1):
            t_next = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t_next

        return t2

if __name__ == "__main__":
    s = Solution()
    # Example 1
    trib1 = s.tribonacci(4)
    print(trib1)  # Output: 4
    # Example 2
    trib2 = s.tribonacci(25)
    print(trib2) # Output: 1389537

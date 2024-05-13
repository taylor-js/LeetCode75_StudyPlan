# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*":
                stack and stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
if __name__ == "__main__":
    s = Solution()
    # Example 1
    s1 = "leet**cod*e"
    rs1 = s.removeStars(s1)
    print(rs1)
    # Example 2
    s2 = "erase*****"
    rs2 = s.removeStars(s2)
    print(rs2)
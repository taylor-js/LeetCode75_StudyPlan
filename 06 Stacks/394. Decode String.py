# https://leetcode.com/problems/decode-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)
    
if __name__ == "__main__":
    sol = Solution()
    # Example 1
    s1 = "3[a]2[bc]"
    ds1 = sol.decodeString(s1)
    print(ds1)
    # Example 2
    s2 = "3[a2[c]]"
    ds2 = sol.decodeString(s2)
    print(ds2)
    # Example 3
    s3 = "2[abc]3[cd]ef"
    ds3 = sol.decodeString(s3)
    print(ds3)
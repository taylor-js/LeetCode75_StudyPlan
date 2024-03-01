# https://leetcode.com/problems/string-compression/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        
        if not chars:
            return 0

        read_index = 0   # pointer for reading from the array
        write_index = 0  # pointer for writing to the array

        while read_index < len(chars):
            current_char = chars[read_index]
            count = 0

            # Count consecutive repeating characters
            while read_index < len(chars) and current_char == chars[read_index]:
                read_index += 1
                count += 1

            # Write the character and its count to the array
            chars[write_index] = current_char
            write_index += 1

            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1

        return write_index

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    chars1 = ["a","a","b","b","c","c","c"]
    comp1 = sol.compress(chars1)
    print(comp1)
    # Example 2
    chars2 = ["a"]
    comp2 = sol.compress(chars2)
    print(comp2)
    # Example 3
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    comp3 = sol.compress(chars3)
    print(comp3)
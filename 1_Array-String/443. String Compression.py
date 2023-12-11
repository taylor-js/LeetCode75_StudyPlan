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

    s = Solution()

    input_str_test_1 = ["a", "a", "b", "b", "c", "c", "c"]

    test_1 = s.compress(input_str_test_1)

    print(test_1)
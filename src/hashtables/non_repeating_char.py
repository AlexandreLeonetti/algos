# non repeating character

def first_unique_char(s):
    char_count = {}  # Hash table to store character frequencies

    # Count occurrences of each character
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1#dict.get(key,default_value_to_return_if_no_key_found)

    # Find first character with frequency 1
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1  # No unique character found

# Example usage
s = "leetcode"
print(first_unique_char(s))  # Output: 0

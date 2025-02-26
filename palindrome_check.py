#palindrome _ check

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:  # If characters don’t match, not a palindrome
            return False
        left += 1
        right -= 1

    return True  # If all characters matched, it’s a palindrome

# Example usage
print(is_palindrome("racecar"))  # ✅ True
print(is_palindrome("hello"))    # ❌ False

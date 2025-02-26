


def palindrome_check(s):
    left =0
    right =len(s)-1

    while left<right:
        if s[left] != s[right]:
            return False
        left+=1
        right-=1


    return True


a = "saas"
b = "sos"

c = "vvvvvv"
d = "abc"

print(a, palindrome_check(a))
print(b, palindrome_check(b))
print(c, palindrome_check(c))
print(d, palindrome_check(d))

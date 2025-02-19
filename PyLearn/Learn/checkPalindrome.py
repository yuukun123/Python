def checkPalindrome(n):
    n = str(n)
    return n == n[::-1]

print(checkPalindrome("abcd"))
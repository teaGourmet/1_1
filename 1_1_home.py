def palindrome(s):
    a = ''.join(reversed(s))
    if s == a:
        return True
    else:
        return False
palindrome('abba')
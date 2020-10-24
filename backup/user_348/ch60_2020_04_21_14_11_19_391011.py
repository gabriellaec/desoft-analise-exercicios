def eh_palindromo (string):
a = string.sort(reverse=True)
if string == a:
    return True
else:
    return False
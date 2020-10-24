def eh_palindromo(string):
    if string.strip() == string.strip()[::-1]:
        return True
    else:
        return False
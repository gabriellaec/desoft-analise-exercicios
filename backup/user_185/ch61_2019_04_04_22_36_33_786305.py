def eh_palindromo(str1,str2):
    if str1[::1] == str2[::-1]:
        return True
    else:
        return False
    
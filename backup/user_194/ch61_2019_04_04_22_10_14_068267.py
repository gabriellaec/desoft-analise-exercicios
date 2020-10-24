def eh_palindromo(string):
    palindromo = False
    if string == string[::-1]:
        palindromo = True
    return palindromo
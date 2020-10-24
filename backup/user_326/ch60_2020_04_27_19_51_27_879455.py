def eh_palindromo(palavra):
    palindromo = palavra[::-1]
    print(palindromo)
    if palindromo == palavra:
        return True
    else:
        return False
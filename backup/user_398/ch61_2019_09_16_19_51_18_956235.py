palavra='ana'
def eh_palindromo(palavra):
    if palavra==palavra[::-1]:
        return True
    else:
        return False

print(eh_palindromo(palavra))        
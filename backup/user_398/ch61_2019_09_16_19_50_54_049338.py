palavra='ana'
def palindromo(palavra):
    if palavra==palavra[::-1]:
        return True
    else:
        return False

print(palindromo(palavra))        
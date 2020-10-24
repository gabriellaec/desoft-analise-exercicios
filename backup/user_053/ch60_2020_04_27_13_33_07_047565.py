def eh_palindromo(palavra):
    nova_palavra = ''
    for i in range(0, len(palavra), -1):
        nova_palavra += i
    if nova_palavra == palavra:
        return True
    else:
        return False
def eh_palindromo(palavra):
    nova_palavra = ''
    for i in range(len(palavra) - 1, -1, -1):
        nova_palavra += palavra[i]
    if nova_palavra == palavra:
        return True
    else: 
        return False
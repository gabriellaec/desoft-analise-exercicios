def verifica_palindromo(palavra):
    teste = ''
    for i in range(0,len(palavra)):
        teste += palavra[len(palavra) - 1 - i]
    return palavra == teste
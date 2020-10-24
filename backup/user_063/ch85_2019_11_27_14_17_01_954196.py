arquivo = open('me-mordam.txt', 'r')
contador = 0
for linha in arquivo:
    linha = linha.rstrip()
    linha = linha.casefold()
    if 'banana' in linha:
        contador += 1
arquivo = open('me-mordam.txt', 'a')
contador = 0
for linha in arquivo:
    linha = linha.rstrip()
    if 'banana' in linha:
        contador += 1
        print (linha)
print (contador)
array = []
arquivo = open('me-mordam.txt', 'r')
contador = 0
for linha in arquivo:
    linha = linha.rstrip()
    linha = linha.casefold()
    array.append(linha)  
    texto = array[0]
    words = texto.split()
    i = 0
    while i < len(words):
        a = i
        if 'banana' in words[a]:
            contador += 1
            a += 1
        else:
            a += 1
        i += 1
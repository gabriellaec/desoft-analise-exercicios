with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    palavras = conteudo.split()
    contador = 0
    i = 0
    while i < len(palavras):
        palavra = palavras[i]
        maiusculo = palavra.upper()
        if palavras[i] == 'BANANA':
            contador = contador + 1
        i = i + 1
print(contador)
            
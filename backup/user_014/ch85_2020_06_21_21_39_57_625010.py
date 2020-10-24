with open('macacos-me-mordam.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    todas_palavras = conteudo.split()
    conta_banana = 0
    while i < len(todas_palavras):
        palavra = todas_palavras[i]
        capitalizando = palavra.upper()
        if capitalizando == 'BANANA':
            conta_bananas += 1
        i += 1
print(conta_banana)   
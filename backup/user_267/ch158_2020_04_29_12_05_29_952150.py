with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()
    p = 0
    for n in lista:
        p += 1
        return p
    
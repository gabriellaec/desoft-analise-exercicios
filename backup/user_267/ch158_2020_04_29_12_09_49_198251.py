with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()
    p = len(lista)
    print(p)

    
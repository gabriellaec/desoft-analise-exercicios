with open('texto.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        texto_lista = conteudo.split()
        i = 0
        for t in texto_lista:
                i += 1
        print(i)
with open('palavras.txt','r') as arquivo:
    conteudo = arquivo.read
    cl = conteudo.lower()
    lista = cl.split()
    lista2 = []
    i = 0
    while i < lista:
        if lista[i][0] == 'a':
        	lista2.append('a')
        	i+=1
    print(len(lista2))
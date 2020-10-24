with open('palavras.txt','r') as arquivo:
    conteudo = arquivo.read
    cl = conteudo.lower()
    lista = cl.split()
    lista2 = []
    contador = 0
    i = 0
    while i < lista:
        if lista[0] == 'a':
        lista2.append('a')
        contador += 1
        i+=1
    print(contador)
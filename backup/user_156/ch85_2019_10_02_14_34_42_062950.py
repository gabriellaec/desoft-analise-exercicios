with open("macacos-me-mordam.txt", "r") as arquivo:
    conteudo = arquivo.read()
    lista = conteudo.split()    
    l1 = []
    i = 0
    while i < len(lista):
        if lista[i] == 'banana':
            l1.append('banana')
        i+=1
    print(len(l1))
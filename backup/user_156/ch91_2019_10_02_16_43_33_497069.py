with open ("palavras.txt", "r") as arquivo:
    conteudo = arquivo.read()
    c1 = conteudo.lower()
    lista = c1.split()
    lista2 = []
    i = 0
    while i < len(lista):
        if lista[i][0] == "a":
            lista2.append("a")
        i+=1
    print (len(lista2))
    
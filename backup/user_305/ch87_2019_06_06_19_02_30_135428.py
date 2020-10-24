with open ("churras.txt","r") as arquivo:
    conteudo = arquivo.read()
    i = 0
    s = 0
    while i< len(conteudo):
        lista = conteudo[i].split(",")
        s += float(lista[i][2]) * int(lista[i][1])
        i +=1
print (s)
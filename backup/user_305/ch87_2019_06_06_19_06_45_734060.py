with open ("churras.txt","r") as arquivo:
    conteudo = arquivo.readlines()
    i = 0
    s = 0
    while i< len(conteudo):
        lista = conteudo[i].split(",")
        s += float(lista[2]) * int(lista[1])
        i +=1
print (s)